from django.conf.urls import url, include
from rest_framework import routers
from bookList import views

router = routers.DefaultRouter()
router.register(r'user', views.UserViewSet)
router.register(r'books', views.BooksViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
