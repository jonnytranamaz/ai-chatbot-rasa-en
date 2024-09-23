FROM python:3.10

USER root

RUN python3 -m pip install rasa

WORKDIR /app

COPY . .

RUN rasa train nlu

USER 1001

ENTRYPOINT ["rasa"]

CMD ["rasa", "run", "--enable-api", "--port", "8080",  "--cors", "*", "--debug"]

