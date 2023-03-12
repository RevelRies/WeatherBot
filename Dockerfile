FROM python:3.10

WORKDIR /weather/WeatherBot

RUN python3 -m pip install --upgrade pip

COPY requirements.txt ./
RUN pip install -r requirements.txt

CMD ["python", "bot.py"]

