FROM python:3
WORKDIR /app
COPY 3.python/ /app
RUN pip3 install -r requirements.txt
CMD sleep 5;python3 manage.py migrate;python3 manage.py runserver 0.0.0.0:8000
