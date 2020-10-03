from rest_framework import serializers
from PointziChallenge.bookList.models import Books, User


class BooksSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Books
        fields = ('ISBN', 'reader', 'title', 'author', 'dateAdded')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ('firstName', 'email', 'country')
