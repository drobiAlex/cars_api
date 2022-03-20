# Cars API

## Run API service in Docker

To run docker container:

- build image: `docker build -t cars-api .`
- run container: `docker run -p 8000:8000 cars-api`

To stop the container:
- stop container: `docker stop cars-api`

Service will be available on http://localhost:8000/