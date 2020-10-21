prerequisites
-------------
- postgresql
- python3
- psycopg2
- django

run commands
------------
- database : sudo service postgresql start
- webserver : python3 manage.py runserver

model editation
---------------
- change models in models.py
- python3 manage.py makemigrations -> create delta files
- python3 manage.py migrate -> apply delta files