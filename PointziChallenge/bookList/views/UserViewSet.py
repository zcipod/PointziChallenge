from PointziChallenge.bookList.serializers import UserSerializer
from rest_framework import viewsets
from PointziChallenge.bookList.models import User


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
