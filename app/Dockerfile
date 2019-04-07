FROM python:3.7-alpine

WORKDIR /application

COPY requirements.txt /application
RUN pip install -r requirements.txt

COPY . /application

ENTRYPOINT ["python"]
CMD ["app.py"]