FROM python:3.8-slim-buster

ENV FLASK_APP=flask_app.py

WORKDIR /code
RUN mkdir tmp

COPY . .

EXPOSE 5000

RUN pip3 install -r requirements.txt

CMD ["flask", "run", "--host", "0.0.0.0", "-p", "5000"]

