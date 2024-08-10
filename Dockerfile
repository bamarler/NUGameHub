FROM python:3.12-alpine3.19
LABEL maintainer="spade.com"

ENV PYTHONUNBUFFERED 1

COPY .requirements.txt /requirements.txt
COPY ./app /spade

WORKDIR /spade
EXPOSE 8000

RUN python -m venv /py && \
    /py/bin/pip install --upgrade pip && \
    /py/bin/pip install -r /requirements.txt && \
    adduser --disabled-password --no-create-home app

ENV PATH="/py/bin:$PATH"

USER app