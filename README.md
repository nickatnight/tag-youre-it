# tag-youre-it :runner:

1. Clone repo `git clone https://github.com/nickatnight/tag-youre-it`
2. `cd tag-youre-it`
3. `mv .env_example .env` to add environment variables as needed
4. Install [Docker](https://www.docker.com/products/docker-desktop)
5. `docker build -t tag-youre-it:latest .`
6. `docker run --env-file .env tag-youre-it:latest`

## Development
Requires [Poetry](https://python-poetry.org/docs/#osx--linux--bashonwindows-install-instructions) to manage dev environment.  Once installed:
1. install packages with `poetry install`
2. black `poetry run black .`
3. flake8 `poetry run flake8`
4. test `poetry run pytest --cov=tag_youre_it tests/`
5. build sdist `poetry build --format sdist`
6. create new setup.py
    ```shell
    $ tar -xvf dist/*-`poetry version -s`.tar.gz -O '*/setup.py' > setup.py
