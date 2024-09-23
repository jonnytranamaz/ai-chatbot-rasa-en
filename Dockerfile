FROM python:3.10

RUN python3 -m pip install rasa

COPY . .

RUN rasa train

USER ai_chatbot_intern

ENTRYPOINT ["rasa"]

CMD ["rasa", "run", "--enable-api", "--port", "8080",  "--cors", "*", "--debug"]

