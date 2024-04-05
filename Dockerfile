FROM python:3.12-slim

WORKDIR /app

#COPY pip.conf /root/.config/pip/pip.conf

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

CMD [ "flask", "run", "-h", "0.0.0.0", "-p", "5000" ]
