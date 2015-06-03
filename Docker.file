FROM python:3.4
WORKDIR /code
ADD . /code
ENV DJANGO_DEBUG=yeah
RUN pip install -r requirements.txt

CMD python manage.py runserver 0.0.0.0:8000

 