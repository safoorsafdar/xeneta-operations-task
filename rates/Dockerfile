FROM python:3.7-slim

WORKDIR /opt/code

COPY requirements.txt requirements.txt
RUN pip install -Ur requirements.txt
RUN pip install -U gunicorn

COPY . .

# CMD ["gunicorn", "-b", "3000", "wsgi"]