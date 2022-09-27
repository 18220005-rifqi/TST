FROM python:3.9.12-slim


EXPOSE 8000

WORKDIR /usr/src/tst

ENV PORT 8000
ENV HOST "0.0.0.0"

COPY ./main.py /app
COPY ./requirments.txt /app

WORKDIR /app


CMD ["uvicorn", "main:app", "--host=0.0.0.0", "--reload"]