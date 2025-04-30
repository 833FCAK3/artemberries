FROM python:3.13.2-slim-bookworm

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV POETRY_VERSION=2.1.2

RUN apt-get update \
    && apt-get -y upgrade \
    && apt-get autoclean && apt-get autoremove \
    && rm -rf /var/lib/apt/lists/* \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && pip install "poetry==$POETRY_VERSION" \
    && poetry config virtualenvs.create false

COPY poetry.lock /src/catalog_service/poetry.lock
COPY pyproject.toml /src/catalog_service/pyproject.toml

RUN mkdir -p /src/catalog_service/
RUN cd /src/catalog_service/ && poetry install
COPY src/ /src/
WORKDIR /src/

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.11.0/wait /wait
RUN chmod +x /wait
