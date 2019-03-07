FROM python:3.7

EXPOSE 5000

WORKDIR /application

COPY requirements.txt /application
RUN pip install -r requirements.txt

COPY . /application

ENTRYPOINT ["python"]
CMD ["app.py"]