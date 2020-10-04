from behave import *


@given('a user "testUser3", and a book "Algorithms"')
def step_impl(context):
    data = {
        "firstName": "testUser3",
        "email": "testUser3@email.com",
        "country": "Australia"
    }
    context.response = context.test.client.post('/user/', data=data)
    dataBooks = {
        "ISBN": "9780321573513",
        "reader": ["http://testserver/user/testUser3/"],
        "title": "Algorithms",
        "author": "Robert Sedgewick",
        "dateAdded": "2020-10-01"
    }
    context.response = context.test.client.post('/books/', dataBooks)


@when('he changes the "dateAdded" from 2020-10-01 to {data:S}')
def step_impl(context, data):
    dataBooks = {
        "ISBN": "9780321573513",
        "reader": ["http://testserver/user/testUser3/"],
        "title": "Algorithms",
        "author": "Robert Sedgewick",
        "dateAdded": data
    }
    context.response = context.test.client.put('/books/9780321573513/', data=dataBooks, content_type="application/json")


@then('the modify status code is {status_code:S}')
def step_impl(context, status_code):
    code = context.response.status_code
    assert str(code) == status_code, "{} != {}".format(code, status_code)


@then('"{date:S}" will be appeared in the response')
def step_impl(context, date):
    assert date in context.response.data.values()


@then('"{title:S}" existing in the last {period:S} days list is {expect}')
def step_impl(context, title, period, expect):
    context.response = context.test.client.get('/books/?firstName=testUser3&period={}'.format(period))
    existed = False
    expect = (expect == "True")
    if context.response.data:
        for book in context.response.data:
            if title in book.values():
                existed = True
                break
    assert existed is expect


@when('he removes the book')
def step_impl(context):
    context.response = context.test.client.delete('/books/9780321573513/')


@then('"{title:S}" will be no longer appeared in the books database')
def step_impl(context, title):
    context.response = context.test.client.get('/books/')
    existed = False
    if context.response.data:
        for book in context.response.data:
            if title in book.values():
                existed = True
                break
    assert existed is False


@when('he removes the account')
def step_impl(context):
    context.response = context.test.client.delete('/user/testUser3/')


@then('"{title:S}" will be no longer appeared in the user database')
def step_impl(context, title):
    context.response = context.test.client.get('/user/')
    existed = False
    if context.response.data:
        for book in context.response.data:
            if title in book.values():
                existed = True
                break
    assert existed is False