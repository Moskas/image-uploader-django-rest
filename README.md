# Image Uploader API

An app based on Django Rest framework.

## Technologies Used

- Python 3.10
- Django 4.1.7
- Redis 7.0.12
- Celery 5.2.7
- Django REST 3.14
- Sqlite 3.41

## Setup

If you are using nix/NixOS with flakes enabled you can run the following command to enter development enviroment:

```bash
nix develop
```

Then you can run the default Django command to start the server:

```bash
python manage.py runserver 8000
```

Any other platform needs to manually download and install needed dependencies listed above.

## Features Implemented

- users can upload images via HTTP request
- admins can create arbitrary tiers with the following things configurable:
  - `arbitrary thumbnail sizes`
  - `presence of the link to the originally uploaded file`
- admin UI has been done via django-admin
