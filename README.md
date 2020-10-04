## Pointzi Full Stack Developer Programming Challenge

This is a solution of a simple Django Rest Framework API program.

This application is a recorder for users to save books they read.

### Deployed practice

the project was [deployed on AWS](http://52.65.111.160:8000).

### API

[Swagger](https://app.swaggerhub.com/apis-docs/zcipod/pointzi-full_stack_developer_programming_challenge/1.1) 

path: "/swagger"  ->   Swagger documentation

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

### Deployment

This project is can be deploied by docker.

To deploy by the following steps:

1. make sure you have correctly installed docker server.
2. switch to the root dir of this project.
3. execute ```docker-compose up``` to start deployment.
4. once you changed the code, execute ```docker-compose up --build``` to rebuild the image.

