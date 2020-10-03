from bookList.serializers import UserSerializer, BooksSerializer
from rest_framework import viewsets
from bookList.models import Books, User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


class BooksViewSet(viewsets.ModelViewSet):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer
