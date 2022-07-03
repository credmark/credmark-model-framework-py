FROM python:3.10

WORKDIR /usr/local/app

COPY . .
RUN pip install .

CMD [ "credmark-dev" ]