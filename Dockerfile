FROM python:3.4
WORKDIR /code
ADD requirements.txt /code/
RUN pip install -r requirements.txt
ADD . /code
WORKDIR /code/app
CMD python manage.py runserver 0.0.0.0:8000

 