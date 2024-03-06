FROM python:3.11.3-slim-buster

COPY ../requirements-dev.txt ./app/requirements-dev.txt
COPY ../src                  ./app/src

RUN apt-get update && apt-get install
RUN pip install -r ./app/requirements-dev.txt

ENV PYTHONPATH=./app/src

EXPOSE 8000

CMD ["python", "-O", "./app/src/simple_clients_api/manage.py", "runserver", "0.0.0.0:8000"]
