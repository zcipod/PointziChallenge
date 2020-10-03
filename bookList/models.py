from django.db import models
from bookList.LIST_OF_COUNTRIES import listOfCountries
import datetime


COUNTRIES = [(item, item) for item in listOfCountries]


class User(models.Model):
    firstName = models.CharField(primary_key=True, max_length=50)
    email = models.EmailField(max_length=50, default="")
    country = models.CharField(choices=COUNTRIES, default='Australia', max_length=50)

    def __str__(self):
        return self.firstName


class Books(models.Model):
    ISBN = models.CharField(max_length=13, primary_key=True)
    reader = models.ManyToManyField(User)
    title = models.CharField(max_length=50, default="None")
    author = models.CharField(max_length=50, default="None")
    dateAdded = models.DateField(auto_now_add=False, default=datetime.date.today())

    def __str__(self):
        return self.title
