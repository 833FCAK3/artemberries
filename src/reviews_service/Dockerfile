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

COPY poetry.lock /src/reviews_service/poetry.lock
COPY pyproject.toml /src/reviews_service/pyproject.toml

RUN mkdir -p /src/reviews_service/
RUN cd /src/reviews_service/ && poetry install
WORKDIR /src/reviews_service/
COPY src/reviews_service/ /src/reviews_service/

ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.11.0/wait /wait
RUN chmod +x /wait
