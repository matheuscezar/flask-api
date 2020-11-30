FROM python:3.7
RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code
EXPOSE 5000
RUN pip install -r requirements.txt
ADD . /code
