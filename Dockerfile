FROM python:3.11.4-slim-bullseye
# sukelia iš source į docker/app
COPY . /main
WORKDIR /main
RUN apt-get update
RUN apt-get install build-essential -y
RUN apt-get install libjpeg-dev -y
RUN apt-get install zlib1g-dev -y
RUN pip install -r requirements.txt
ENTRYPOINT gunicorn run:app -b 0.0.0.0