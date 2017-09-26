FROM fedora:latest

RUN dnf -y update
RUN dnf -y install wget tar git
RUN python3 -m pip install Flask flask_script
RUN mkdir /Dev

WORKDIR /Dev
RUN git clone https://github.com/promogekko/json-server.git

WORKDIR /Dev/json-server

EXPOSE 5000

ENTRYPOINT ["python3","json-server.py","runserver"]
CMD ["-h=0.0.0.0"]
