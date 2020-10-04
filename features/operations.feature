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