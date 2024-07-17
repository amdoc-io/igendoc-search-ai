FROM --platform=linux/amd64 python:3.10-alpine AS builder

WORKDIR /igendoc-search-ai

COPY . /igendoc-search-ai

RUN pip3 install -r requirements.txt

CMD ["gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "app.app:app"]