from django.core.validators import RegexValidator
from django.db import models
from PointziChallenge.bookList.LIST_OF_COUNTRIES import listOfCountries
import datetime


COUNTRIES = [(item, item) for item in listOfCountries]


class User(models.Model):
    firstName = models.CharField(
        primary_key=True,
        max_length=16,
        validators=[
            RegexValidator(
                regex='^([a-zA-Z0-9_]{4,16})$',
                message='input invalid, 4-16 chars in numbers, letters or _'
            )
        ]
    )
    email = models.EmailField(max_length=50, default="")
    country = models.CharField(choices=COUNTRIES, default='Australia', max_length=50)

    def __str__(self):
        return self.firstName


class Books(models.Model):
    ISBN = models.CharField(
        max_length=13,
        primary_key=True,
        validators=[
            RegexValidator(
                regex='^([0-9]{10,13})$',
                message='input invalid, 10 or 13 numbers'
            )
        ]
    )
    reader = models.ManyToManyField(User)
    title = models.CharField(max_length=50, default="None")
    author = models.CharField(max_length=50, default="None")
    dateAdded = models.DateField(auto_now_add=False, default=datetime.date.today())

    def __str__(self):
        return self.title
