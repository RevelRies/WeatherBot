FROM python:3.10

COPY . .
WORKDIR .

RUN python3 -m pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

CMD ["python3", "bot.py"]

