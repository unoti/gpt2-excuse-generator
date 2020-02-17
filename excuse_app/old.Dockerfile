FROM python:3-alpine

RUN mkdir /app
WORKDIR /app

# This is so we can do print() from Python without having to flush stdout afterward.
ENV PYTHONUNBUFFERED 1

COPY requirements.txt /app

# Install dependencies so we can do the pip install. Then remove them to keep image size down.
RUN apk add --no-cache build-base libressl-dev musl-dev libffi-dev && \
    pip install --no-cache-dir -r requirements.txt && \
    apk del build-base musl-dev libffi-dev

COPY . /app

# Expose the flask port
EXPOSE 5000

CMD [ 'python', './app.py' ]
