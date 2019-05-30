LOOP
===================
## Description
Loop is a web application that allows users to keep in touch wiyh everything going on in the neighbourhood. Members can post incidents in their respective neighbourhoods, get security information, as wee as business info.

------------------------------------------------------------------------

## Features

+ [x] Posting incidents that have occurred in the neeighbourhood.
+ [x] Grouping users in respective neighbourhoods.
+ [x] Business and service providers can be advertised.
+ [x] users can switch neighbourhoods when they move out.
+ [x] User authentication system: login and sign up.
+ [x] Django admin dashboard for site management.



## Getting started

### Requirements
This project was created on a debian linux platform but should work on other unix based[not limited to] sytems.
* Tested on Debian Linux
* Python3

### Cloning the repository
```bash
git clone https://github.com/IJaccojwang/loop.git && cd loop
```

### Creating a virtual environment

```bash
python3 -m virtualenv virtual
source virtual/bin/activate
```
### Installing dependencies
```bash
pip3 install -r requirements
```

### Prepare environmet variables
For this project you will need the following configurations plus email setup for email registration hmac verification.
```python
SECRET_KEY= #secret key will be added by default
DEBUG= #set to false in production
DB_NAME= #database name
DB_USER= #database user
DB_PASSWORD=#database password
DB_HOST="127.0.0.1"
MODE= # dev or prod , set to prod during production
ALLOWED_HOSTS='.localhost', '.herokuapp.com', '.127.0.0.1'
```

### Database migrations

```bash
python manage.py migrate
```

### Running the server
```bash
python manage.py runserver
```

### Admin Dashboard
Use django admin to manage the different users and posts.


## Running the tests
```bash
python manage.py test
```

## Live Demo

The web app can be accessed from the following link:
[Loop](https://ijloop.herokuapp.com/)


## Technology used

* [Python3.6](https://www.python.org/)
* [Django 1.11](https://www.djangoproject.com/)
* [Heroku](https://heroku.com)

## Behaviour driven development/ Specifications

| Behaviour |  Sample Input | Sample Output |
| :---------------- | :---------------: | :------------------ |
| Join a neighbourhood| On sign up | You are added to the neighbourhood you select |
| View Neighbourhood posts| On login | All posts displayed |
| Search businesses| Submit search form | All businesses meeting the criteria are displayed|
| Post new incident | Submit newincident/announcement form| Post uploaded, view on feed|
| Leave a neighbourhood | Move out form | User moved to different neighbourhood|



## Contributing

- Git clone [https://github.com/IJaccojwang/loop.git](https://github.com/IJaccojwang/loop.git)
- Make the changes.
- Write your tests.
- If everything is OK. push your changes and make a pull request.

## License ([MIT License](http://choosealicense.com/licenses/mit/))
This project is licensed under the MIT Open Source license, (c) [Ian Jaccojwang](https://github.com/IJaccojwang)
