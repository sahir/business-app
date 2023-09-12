**  Business Module **

### Setup Instruction & Uses

1. Create docker build image

`docker build -t business_app .`

2. Run the Docker image

`docker run -it -p 8000:8000 -v .:/code business_app`

3. Navigate on the http://localhost:8000/api/docs or http://IP-Address:8000/api/docs

### Run The test

`pytest --cov=app tests.py`
