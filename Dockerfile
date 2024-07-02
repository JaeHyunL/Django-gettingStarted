FROM python:3.11

ENV PYTHONBUFFERED 1

ARG DEV=false

COPY requirements.txt /app/
COPY requirements-dev.txt /app/
COPY app /app/

WORKDIR /app
RUN pip install -r requirements.txt

RUN if [ "$DEV" = "true" ]; then pip install -r requirements-dev.txt; fi

EXPOSE 8000
