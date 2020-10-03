from django.conf.urls import url, include
from django.urls import path
from rest_framework import routers
from PointziChallenge.bookList import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'books', views.BooksViewSet)

urlpatterns = [
    path('swagger', views.swagger),
    url(r'^', include(router.urls)),
]
