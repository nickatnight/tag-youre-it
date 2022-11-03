# docker
init-db:
	docker compose run --rm tag alembic -c tag_youre_it/alembic.ini revision --autogenerate -m "init"

migrations:
	docker compose run --rm tag alembic -c tag_youre_it/alembic.ini revision --autogenerate

migrate:
	docker compose run --rm tag alembic -c tag_youre_it/alembic.ini upgrade head

up:
	docker compose up

down:
	docker compose down

test:
	docker compose exec tag pytest --cov=tag_youre_it

bash:
	docker compose exec tag bash

db-shell:
	docker compose exec db psql -U tagyoureit -d tagyoureit

volume-rm:
	docker volume rm tag-youre-it_db-data --force

# poetry
black:
	poetry run black .

flake8:
	poetry run flake8

mypy:
	poetry run mypy tag_youre_it

isort:
	poetry run isort .

bundle:
	poetry build --format sdist
	tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/
