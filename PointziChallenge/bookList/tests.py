from rest_framework import status
from rest_framework.test import APITestCase
from PointziChallenge.bookList import models
from PointziChallenge.bookList import views
import datetime


class ApiTests(APITestCase):
    def setUp(self):
        url = '/user/'
        data = {
            "firstName": "testUser1",
            "email": "testUser1@email.com",
            "country": "Australia"
        }
        data2 = {
            "firstName": "testUser2",
            "email": "testUser2@email.com",
            "country": "Australia"
        }
        self.response = self.client.post(url, data, format='json')
        self.response = self.client.post(url, data2, format='json')

        urlBooks = '/books/'
        dataBooks = {
            "ISBN": "9781491946008",
            "reader": ["testUser1"],
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": "2020-10-01"
        }
        self.responseBooks = self.client.post(urlBooks, dataBooks, format='json')

    def test_createUser(self):
        data = {
            "firstName": "testUser2",
            "email": "testUser2@email.com",
            "country": "Australia"
        }
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.User.objects.count(), 2)
        self.assertEqual(dict(self.response.data), data)

    def test_listUser(self):
        url = '/user/'
        response = self.client.get(url)
        data = {
            "firstName": "testUser1",
            "email": "testUser1@email.com",
            "country": "Australia"
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)
        self.assertEqual(dict(response.data[0]), data)

    def test_updateUser(self):
        url = '/user/testUser1/'
        data = {
            "firstName": "testUser1",
            "email": "testUser2@email.com",
            "country": "Australia"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), data)

    def test_removeUser(self):
        url = '/user/testUser1/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.User.objects.count(), 1)

    def test_retrieveUser(self):
        url = '/user/testUser1/'
        data = {
            "firstName": "testUser1",
            "email": "testUser1@email.com",
            "country": "Australia"
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), data)

    def test_listWithFirstName(self):
        response = views.listWithFirstName('testUser1')
        data = {
            "ISBN": "9781491946008",
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": datetime.date(2020, 10, 1)
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], data)

    def test_checkISBNOnGoogleBook(self):
        response = views.checkISBNOnGoogleBook('9781491946008')
        self.assertEqual(response['items'][0]['volumeInfo']['title'], "Fluent Python")

    def test_listWithFirstNameAndPeriod(self):
        response = views.listWithFirstNameAndPeriod('testUser1', 7)
        data = {
            "ISBN": "9781491946008",
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": datetime.date(2020, 10, 1)
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0], data)

    def test_createBook(self):
        dataBooks = {
            "ISBN": "9781491946008",
            "reader": ['http://testserver/user/testUser1/'],
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": '2020-10-01'
        }
        self.assertEqual(self.responseBooks.status_code, status.HTTP_201_CREATED)
        self.assertEqual(models.Books.objects.count(), 1)
        self.assertEqual(dict(self.responseBooks.data), dataBooks)

    def test_listBooks(self):
        url = '/books/'
        response = self.client.get(url)
        data = {
            "ISBN": "9781491946008",
            "reader": ['http://testserver/user/testUser1/'],
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": '2020-10-01'
        }
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(dict(response.data[0]), data)

    def test_retrieveBooks(self):
        url = '/books/9781491946008/'
        data = {
            "ISBN": "9781491946008",
            "reader": ['http://testserver/user/testUser1/'],
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": '2020-10-01'
        }
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), data)

    def test_updateBook(self):
        url = '/books/9781491946008/'
        data = {
            "ISBN": "9781491946008",
            "reader": ['http://testserver/user/testUser1/',
                       'http://testserver/user/testUser2/'],
            "title": "Fluent Python",
            "author": "Luciano Ramalho",
            "dateAdded": '2020-10-02'
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(dict(response.data), data)

    def test_removeBook(self):
        url = '/books/9781491946008/'
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(models.Books.objects.count(), 0)
