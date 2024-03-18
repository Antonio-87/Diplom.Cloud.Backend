# My cloud

## Description

Cloud storage where you can store your files, download and use their links to put in other
services.

Backend - https://github.com/Antonio-87/Diplom.Cloud.Backend.git<br />
Frontend - https://github.com/Antonio-87/Diplom.Cloud.Frontend.git

- File managing:
  - Save files in current location or into a folder.
  - Add notes.
  - Change file name, notes.
  - Download file.
  - Copy permalink.
- User profile:
  - Create new profile.
  - Delete profile.
  - Change Username, Full Name, Email, Password.
  - Track files count and total space.
- Storage max size is 2Gb for each user.
- Admin profile:
  - List of all active users (without current user).
  - Manage other users:
    - Change other user admin status.
    - Delete other user account.
  - Manage other users storage:
    - List of all user files.
    - Delete file.
    - Change file name, notes.
    - Download file.

## Toolset

- Django
- Django Rest Framework
- Simple JWT
- Postgresql
- Pytest

## API

User:

- GET "api/users/" --> list of users
  - admin token required
- POST "api/users/" --> create new user
  - required fields: username, full_name, email, password, repeat_password
- GET "api/users/\<pk>/" --> get user
  - token required
- PUT, PATCH "api/users/update/\<pk>/" --> update user
  - token required
  - fields: username, full_name, email
  - password change required fields: current_password, password, repeat_password
- DELETE "api/users/delete/\<pk>/" --> delete user
  - token required
  - fields: username, full_name, email

Tokens:

- POST "api/token/" --> get new access and refresh token
  - required fields: username, password
- POST "api/token/refresh/" --> get new access token
  - required fields: refresh
- POST "api/token/verify/" --> verify access token
  - required fields: token

Storage:

- GET "api/storages/" --> list of storages
  - admin token required
- GET "api/storages/\<pk>/" --> get storage
  - token required

File:

- POST "api/files/" --> create new file
  - token required
  - required fields: file_data, name
  - optional fields: path, note
- PUT, PATCH "api/files/update/\<pk>/" --> update file
  - token required
  - fields: name, note
- DELETE "api/files/delete/\<pk>/" --> delete file
  - token required

## env

- Configure variables:
  - SECRET_KEY=
  - DEBUG=0
  - ALLOWED_HOSTS=\<server ip address>
  - ALLOWED_CORS_ORIGINS=http://\<server ip address>,https://\<server ip address>
  - DB_ENGINE=django.db.backends.postgresql
  - DB_NAME=\<db_name>
  - DB_HOST=localhost
  - DB_PORT=5432
  - DB_USER=\<username>
  - DB_PASSWORD=\<password>
