install:
	poetry install
	poetry run python manage.py makemigrations
	poetry run python manage.py migrate

run:
	poetry run python manage.py runserver

test:
	poetry run python manage.py test