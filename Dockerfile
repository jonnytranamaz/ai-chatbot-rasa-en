FROM python:3.10

USER root

RUN python3 -m pip install rasa

WORKDIR /app

COPY . .

RUN rasa train nlu

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml

USER 1001

ENTRYPOINT ["rasa"]

CMD ["rasa", "run", "--enable-api", "--port", "9003",  "--cors", "*", "--debug"]

