FROM --platform=linux/amd64 python:3.10-alpine AS builder

WORKDIR /igendoc-search-ai

COPY . /igendoc-search-ai

RUN pip3 install -r requirements.txt

CMD ["python3", "app/app.py"]