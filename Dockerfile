FROM python:3.11

WORKDIR /usr/local/app

COPY . .
RUN pip install .

CMD [ "credmark-dev" ]