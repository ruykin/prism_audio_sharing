# prism_audio_sharing
World Music Hackathon submission: Secure audio sharing to control piracy.

## Requirements
- Python <= 3.7.5
- Pip <= 19.0.3

## Project Setup
- Install `pipenv`
  ```bash
  pip install pipenv
  ```
  
- Setup Environment
  ```bash
  pipenv install
  ```
  
- Run Migrations.
  ```bash
  python manage.py makemigrations && python manage.py migrate
  ```

- Crete Superuser
  ```bash
  python manage.py createsuperuser
  ```
  
- Run Server
  ```bash
  python manage.py runserver
  ```
  
## How to use
- Access admin panel to add users.
    `http://127.0.0.1:8000/admin/`
