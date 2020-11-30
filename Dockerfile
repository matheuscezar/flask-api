FROM python:3.7
RUN mkdir /code
WORDIR /code
ADD requirements.txt /code
RUN pip install -r requirements.txt
ADD . /code