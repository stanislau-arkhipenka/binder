FROM python:3-alpine

LABEL MAINTAINER="Stanislau Arkhipenka"

WORKDIR /code
COPY requirements.txt /code/requirements.txt

RUN apk add --no-cache nsd build-base python3-dev libffi-dev openssl-dev libc-dev libxslt-dev mariadb-connector-c-dev \
  && pip install --upgrade pip \
  && pip install --no-cache-dir -r requirements.txt

COPY . /code/

EXPOSE 8000

RUN ["python", "manage.py", "makemigrations", "binder"]
RUN ["python", "manage.py", "migrate"]
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
