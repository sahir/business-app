FROM python:3.9
RUN apt-get update
RUN apt-get --yes install libsndfile1-dev

COPY . /code
WORKDIR /code
RUN pip install --no-cache-dir -r /code/requirements.txt

EXPOSE 8000
CMD uvicorn app:app --host 0.0.0.0 --port 8000