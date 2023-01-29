FROM python:3.11-slim-bullseye

RUN mkdir /app
COPY src/ /app
WORKDIR /app
RUN pip3 install -r requirements.txt
RUN useradd -M -r ctfuser

USER ctfuser
CMD ["python3", "/app/app.py"]