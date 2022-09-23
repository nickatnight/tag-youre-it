FROM python:3.9 as base

WORKDIR /tmp

RUN pip install poetry

COPY ./pyproject.toml ./poetry.lock* /tmp/

RUN poetry export -f requirements.txt --output requirements.txt --without-hashes

FROM python:3.9

COPY --from=base /tmp/requirements.txt /code/requirements.txt

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY . /code/

ENV PYTHONPATH "${PYTHONPATH}:/code"

WORKDIR /code/tag_youre_it
CMD ["python3", "./play.py"]
