FROM python:3.12

RUN mkdir /ration_master_backend

WORKDIR /ration_master_backend

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD uvicorn main:app --host 0.0.0.0 --port 8080
