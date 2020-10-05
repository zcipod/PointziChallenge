from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from PointziChallenge.bookList.views import UserViewSet, BooksViewSet, Swagger

router = routers.DefaultRouter()
router.register(r'user', UserViewSet.UserViewSet)
router.register(r'books', BooksViewSet.BooksViewSet)

urlpatterns = [
    path('swagger', Swagger.swagger),
    url(r'^', include(router.urls)),
]
