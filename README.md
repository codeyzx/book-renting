## PIZZA DELIVERY API

This is a REST API for a Book renting service built for fun and learning with FastAPI, SQLAlchemy and PostgreSQL.

## ROUTES TO IMPLEMENT

| METHOD   | ROUTE                               | FUNCTIONALITY                    | ACCESS      |
| -------- | ----------------------------------- | -------------------------------- | ----------- |
| _POST_   | `/auth/signup/`                     | _Register new user_              | _All users_ |
| _POST_   | `/auth/jwt/create/`                 | _Login user_                     | _All users_ |
| _POST_   | `/auth/jwt/refresh/`                | _Refresh the access token_       | _All users_ |
| _POST_   | `/auth/jwt/verify/`                 | _Verify the validity of a token_ | _All users_ |
| _POST_   | `/rents/`                           | _Place an order_                 | _All users_ |
| _POST_   | `/rents/`                           | _Get all orders_                 | _All users_ |
| _GET_    | `/order/{rents_id}/`                | _Retrieve an order_              | _Superuser_ |
| _PUT_    | `/orders/{rents_id}/`               | _Update an order_                | _All users_ |
| _DELETE_ | `/delete/{rents_id}/`               | _Delete/Remove an order_         | _All users_ |
| _GET_    | `/user/{user_id}/rents/`            | _Get user's orders_              | _All users_ |
| _GET_    | `/user/{user_id}/rents/{rents_id}/` | _Get user's specific order_      |
| _GET_    | `/docs/`                            | _View API documentation_         | _All users_ |

## How to run the Project

- Install Postgreql
- Install Python
- Git clone the project with ` git clone https://github.com/codeyzx/book-renting.git`
- Create your virtualenv with `Pipenv` or `virtualenv` and activate it.
- Install the requirements with `pip install -r requirements.txt`
- Create you database with `python manage.py runserver`
- Finally run the API
  ``python manage.py runserver`
