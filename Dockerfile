FROM docker.io/python:3.11
LABEL authors="aiquen"

RUN groupadd -g 1000 webgroup
RUN useradd -u 1000 -m -d /app -s /sbin/nologin -r webuser

COPY --chown=1000:1000 main.py requirements.txt /app/

USER webuser
WORKDIR /app

RUN pip3 install -r requirements.txt

EXPOSE 8081

CMD ["python3", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8081"]