from behave import *


@given("we have the back-end running")
def step_impl(context):
    pass


@when('he adds his information with the firstName of "testUser2"')
def step_impl(context):
    data = {
        "firstName": "testUser2",
        "email": "testUser2@email.com",
        "country": "Australia"
    }
    context.response = context.test.client.post('/user/', data=data)


@then('the status code is {status_code:S}')
def step_impl(context, status_code):
    code = context.response.status_code
    assert str(code) == status_code, "{} != {}".format(code, status_code)


@then('"testUser2" will be appeared in the response')
def step_impl(context):
    assert 'testUser2' in context.response.data.values()


@when('he adds 1 new books(title=Fluent Python)')
def step_impl(context):
    dataBooks = {
        "ISBN": "9781491946008",
        "reader": ["http://testserver/user/testUser2/"],
        "title": "Fluent Python",
        "author": "Luciano Ramalho",
        "dateAdded": "2020-10-01"
    }
    context.response = context.test.client.post('/books/', dataBooks)


@then('the status code is also {status_code:S}')
def step_impl(context, status_code):
    code = context.response.status_code
    assert str(code) == status_code, "{} != {}".format(code, status_code)


@then('"Fluent Python" will be appeared in the response')
def step_impl(context):
    assert 'Fluent Python' in context.response.data.values()


@when('he adds 1 new books(title=Algorithms) with the wrong ISBN {ISBN:S}')
def step_impl(context, ISBN):
    dataBooks = {
        "ISBN": ISBN,
        "reader": ["http://testserver/user/testUser2/"],
        "title": "Algorithms",
        "author": "Robert Sedgewick",
        "dateAdded": "2020-09-25"
    }
    context.response = context.test.client.post('/books/', dataBooks)


@then('the request is denied, the status code is {status_code:S}')
def step_impl(context, status_code):
    code = context.response.status_code
    assert str(code) == status_code, "{} != {}".format(code, status_code)


@when('he adds the new books(title=Algorithms) with the right ISBN {ISBN:S}')
def step_impl(context, ISBN):
    dataBooks = {
        "ISBN": ISBN,
        "reader": ["http://testserver/user/testUser2/"],
        "title": "Algorithms",
        "author": "Robert Sedgewick",
        "dateAdded": "2020-09-25"
    }
    context.response = context.test.client.post('/books/', dataBooks)


@then('the status code is finally {status_code:S}')
def step_impl(context, status_code):
    code = context.response.status_code
    assert str(code) == status_code, "{} != {}".format(code, status_code)


@then('"{title:S}" will finally be appeared in the response')
def step_impl(context, title):
    assert title in context.response.data.values()
