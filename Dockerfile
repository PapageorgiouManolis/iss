FROM python:3.7

MAINTAINER ManolisPapageorgiou

WORKDIR /app
COPY / /app

RUN pip install -r requirements.txt

CMD ["python","app.py"]
