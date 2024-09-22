FROM python:3.10

RUN python3 -m pip install rasa

COPY . .

RUN rasa train nlu

USER 1001

ENTRYPOINT ["rasa"]

CMD ["rasa", "run", "--enable-api", "--port", "8080",  "--cors", "*", "--debug"]

