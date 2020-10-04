## Pointzi Full Stack Developer Programming Challenge

This is a solution of a simple Django Rest Framework API program.

This application is a recorder for users to save books they read.

### Deployed practice

the project was [deployed on AWS](http://52.65.111.160:8000).

### API

path: "/user/"

| method | description|
| ----|----|
| get | get all the users in the database|
| post | create a new user with the information in the body of the query|

path: "/user/{firstName}/"

| method | description|
| ----|----|
| get | retrieve the information of the user with the name of "firstName" |
| put | update the user with the firstName of "firstName" |
| delete | delete the user with the firstName of "firstName" |

path: "/books/"

| method | description                                                  |
| ------ | ------------------------------------------------------------ |
| get    | get all the books in the database<br />option: <br />    ?firstName={firstName}<br />     retrieve all the books that "firstName" has read<br /><br />    ?firstName={firstName}&period={period}<br />     retrieve all the books that "firstName" read in the last "period" of days |
| post   | create a new book record with the information in the body of the query |

path: "/books/{ISBN}/"

| method | description                                                  |
| ------ | ------------------------------------------------------------ |
| get    | retrieve the information of the book with the ISBN of "ISBN" |
| put    | update the book with the ISBN of "ISBN"                      |
| delete | delete the book with the ISBN of "ISBN"                      |

#### Fields validation

##### ISBN

Once create a book record, the ISBN will be validated by Google Book API.

Both 10 digits style and 13 digits style are acceptable.

The API is https://www.googleapis.com/books/v1/volumes?q=isbn:**ISBN**

##### firstName

Only numbers, letters or "_" can be used in firstName of users. The length is between [4, 16]

### Documentation

 -> [Swagger](https://app.swaggerhub.com/apis-docs/zcipod/pointzi-full_stack_developer_programming_challenge/1.1) 

### Unit Test

run unit test:

```python manage.py test```

### BDD Test

Implement Behaviour Driven Development test using [behave](https://github.com/behave/behave) and [behave-django](https://github.com/behave/behave-django)

run BDD Test:

```python manage.py behave```

The [content of the test](./features/operations.feature) is:

```Feature
Feature: general operations to use this back-end

  Scenario: a new user "testUser2" add 2 books

    Given we have the back-end running

      When he adds his information with the firstName of "testUser2"
      Then the status code is 201
        And "testUser2" will be appeared in the response

      When he adds 1 new books(title=Fluent Python)
      Then the status code is also 201
      And "Fluent Python" will be appeared in the response

      When he adds 1 new books(title=Algorithms) with the wrong ISBN 9780321573000
      Then the request is denied, the status code is 400

      When he adds the new books(title=Algorithms) with the right ISBN 9780321573513
      Then the status code is finally 201
      And "Algorithms" will finally be appeared in the response


  Scenario: a user modifies information of a book, then removes it, finally removes his account

    Given a user "testUser3", and a book "Algorithms"

      When he changes the "dateAdded" from 2020-10-01 to 2020-09-01
      Then the modify status code is 200
      And "2020-09-01" will be appeared in the response
      And "Algorithms" existing in the last 7 days list is False

      When he removes the book
      Then "Algorithms" will be no longer appeared in the books database

      When he removes the account
      Then "testUser3" will be no longer appeared in the user database
```

### Deployment

This project is can be deploied by docker.

To deploy by the following steps:

1. make sure you have correctly installed docker server and docker-compose.
2. switch to the root dir of this project.
3. execute ```docker-compose up``` to start deployment.
4. once you changed the code, execute ```docker-compose up --build``` to rebuild the image and deploy.

