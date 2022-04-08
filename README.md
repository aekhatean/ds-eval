# Div-systems assessment

An API that enables you to create users, obtain Tokens for authentication, uses auth tokens to create status for existing users.

## Description

This API Django, coverage, pillow, djangorestframework, django-rest-auth.

## Getting Started

### Dependencies

- This API needs Python and Django to work.
- To install dependencies run the folloing command in the root directory:

```
pip install -r requirements.md
```

### Database migrations

- run the following commands to make database migrations

```
python3 manage.py makemigrations
python3 manage.py migration
```

### running the API

- run the following commands to run the server

```
python3 manage.py runserver
```

### Endpoints

1. `create-user/`:
   - Accepts POST request
   - parameters to pass to this endpoint
     - first_name: String
     - last_name: String
     - country_code: String - Currently accepts (eg, us)
     - phone_number: String - e164 phone number format
     - gender: String - Accents (male, female)
     - birthdate: Date - YYYY-MM-DD
     - password: String
     - email: String - email format
2. `obtain-token/`:
   - Accepts POST request
   - parameters to pass to this endpoint
     - phone_number: String - e164 phone number format (Should Already exist in the database)
     - password: String
3. `create-status/`:
   - Accepts POST request
   - parameters to pass to this endpoint
     - phone_number: String - e164 phone number format (Should Already exist in the database)
     - status: String

### Unit Tests:

- To run the tests, run this command:
  ```
  coverage run --omit='*/venv/*' manage.py test
  ```
- To detect coverage percentage do the following:
  - Run the following command:
    ```
    coverage html
    ```
  - From htmlcov open `index.html`

## Authors

Contributors names and contact info

Adham Khatean

- Github:[@aekhatean](https://github.com/aekhatean)
- Linkedin: [@Adhamkhatean](https://www.linkedin.com/in/adhamkhatean/)

## Version History

- 1.0.0
  - Initial Release
