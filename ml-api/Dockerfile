FROM python:3.12-slim

WORKDIR /app

RUN apt -y update && apt install -y \
  python3-dev \
  apt-utils \
  build-essential \
&& rm -rf /var/lib/apt/lists/*

RUN pip3 install --upgrade setuptools
RUN pip3 install cython==3.0.11 numpy==2.1.3 pandas==2.2.3

COPY . .
RUN pip3 install -r requirements.txt

EXPOSE 5000

CMD ["uvicorn", "app:app", "--host", "localhost", "--port", "5000"]