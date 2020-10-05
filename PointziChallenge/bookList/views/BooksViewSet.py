from django.core.exceptions import ObjectDoesNotExist
from PointziChallenge.bookList.serializers import UserSerializer, BooksSerializer
from rest_framework import viewsets
from PointziChallenge.bookList.models import Books, User
from rest_framework import status
from rest_framework.response import Response
import datetime
import json
from PointziChallenge.bookList.utils.web_page import Web_Page


def listWithFirstName(firstName):
    res = []
    try:
        userObjs = User.objects.get(firstName=firstName)
        for book in userObjs.books_set.all():
            book.__dict__.pop('_state')
            res.append(book.__dict__)
        response = Response(res, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        response = Response({"detail": e.args}, status=status.HTTP_404_NOT_FOUND)
    return response


def listWithFirstNameAndPeriod(firstName, period):
    res = []
    today = datetime.date.today()
    date = today - datetime.timedelta(days=int(period))
    try:
        userObjs = User.objects.get(firstName=firstName)
        bookObjs = Books.objects.filter(reader__firstName=firstName, dateAdded__gte=date)
        for book in bookObjs.all():
            book.__dict__.pop('_state')
            res.append(book.__dict__)
        response = Response(res, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        response = Response({"detail": e.args}, status=status.HTTP_404_NOT_FOUND)
    return response


def checkISBNOnGoogleBook(isbn):
    page = Web_Page()
    checkOnGoogleBookApi = "https://www.googleapis.com/books/v1/volumes?q=isbn:" + isbn
    page.open_url(checkOnGoogleBookApi)
    return json.loads(page.page)


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer

    def list(self, request, *args, **kwargs):
        params = request.query_params.dict()
        if 'firstName' in params:
            if 'period' in params:
                response = listWithFirstNameAndPeriod(params['firstName'], params['period'])
            else:
                response = listWithFirstName(params['firstName'])
        else:
            response = super(viewsets.ModelViewSet, self).list(request, args, kwargs)
        return response

    def create(self, request, *args, **kwargs):
        request.POST._mutable = True
        hostName = request.get_host()
        if isinstance(request.data['reader'], list):
            request.data['reader'] = ["".join(["http://", hostName, '/user/', item, '/'])
                                      if not item.startswith("http://") else item
                                      for item in request.data['reader']]

        checkResult = checkISBNOnGoogleBook(request.data['ISBN'])
        if checkResult['totalItems']:
            response = super(viewsets.ModelViewSet, self).create(request, args, kwargs)
        else:
            response = Response({'detail': "Can't find the ISBN on Google Book. Please double-check it!"},
                                status=status.HTTP_400_BAD_REQUEST)
        return response
