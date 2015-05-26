FROM python:3.4
WORKDIR /code
ADD requirements.txt /code/
ADD requirements.fullstack.txt /code/
RUN pip install -r requirements.fullstack.txt
ADD . /code
WORKDIR /code/app
ENV SVFROEMERN_FULLSTACK=true
CMD python manage.py runserver 0.0.0.0:8000

 