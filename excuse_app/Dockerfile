FROM pytorch/pytorch:latest

# This is so we can do print() from Python without having to flush stdout afterward.
ENV PYTHONUNBUFFERED 1

# Removed  --cuda_ext
RUN git clone https://github.com/NVIDIA/apex.git && cd apex && python setup.py install --cpp_ext

#RUN pip install transformers

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

#RUN mkdir /app
WORKDIR /app
#COPY requirements.txt /app
#RUN pip install --no-cache-dir -r requirements.txt

#COPY . /app

# Expose the flask port
EXPOSE 5000

CMD [ 'python', './app.py' ]
