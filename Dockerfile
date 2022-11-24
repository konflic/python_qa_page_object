FROM python:3.10-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install -U pip
RUN pip install -r requirements.txt

EXPOSE 80

COPY . .

CMD ["pytest", "--browser", "chrome"]