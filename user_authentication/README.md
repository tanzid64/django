# User Authentication
A basic user authentication project using django framework.

## Features
- Custom User model
- Registration, Get all user's details, Get single user's details, Login, Update user details, Delete account.
- Token authentication.

## API Documentaion
Postman Api documentation: https://documenter.getpostman.com/view/32603042/2sA3Bj7DfR

## Deployment

The first thing to do is to clone the repository:

```bash
  git clone https://github.com/tanzid64/blood-bank.git
  cd blood-bank
```
Create a virtual environment to install dependencies in and activate it:
- For windows:
```bash
  python -m venv .venv
  .venv\Scripts\activate
```
- For Ubuntu:
```bash
  virtualenv .venv
  .venv/bin/activate
```
Then install the dependencies:

```bash
  pip install -r requirements.txt
```

Apply migrations:

```bash
  python manage.py migrate
```
Create an admin account:

```bash
  python manage.py createsuperuser
```
Start the django application::

```bash
  python manage.py runserver
```

That's it! You should now be able to see the demo application.
Browse:
- HomePage:  localhost:8000/
- Admin Panel:  localhost:8000/admin
