FROM python:3.9.13

WORKDIR /usr/src/app/django/muit-takenoko

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY . .