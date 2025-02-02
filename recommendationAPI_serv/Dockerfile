FROM python:slim

RUN mkdir -p /usr/src/app
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app/

RUN pip3 install --upgrade pip

RUN pip3 install --no-cache-dir -r requirements.txt

RUN pip install numpy

COPY . /usr/src/app

EXPOSE 8081

ENTRYPOINT ["python3"]

CMD ["-m", "swagger_server"]