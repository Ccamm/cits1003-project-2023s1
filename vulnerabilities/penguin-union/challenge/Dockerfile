FROM python:3.10.5-slim-bullseye
ARG LAB_TYPE

RUN mkdir -p /penguin-os
COPY ./requirements.txt /penguin-os/requirements.txt
RUN pip3 install -r /penguin-os/requirements.txt

COPY . /penguin-os
WORKDIR /penguin-os

USER www-data
CMD ["python3", "app.py", "--host", "0.0.0.0"]