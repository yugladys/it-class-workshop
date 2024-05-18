# Demo API

This is a simple API using FastAPI for workshop/demo use.

## About the API

### Environment Variables

| Variable | Description         | Sample Value |
|----------|---------------------|--------------|
| APP_HOST | hostname of the app | 0.0.0.0      |
| APP_PORT | port of the app     | 80           |

### Endpoints

| Endpoint | Method | Description  |
|----------|--------|--------------|
| /healthz | GET    | health check |
| /hello   | GET    | hello world  |

## Running the API

```sh
uvicorn main:app
```

```sh
uvicorn main:app --host ${APP_HOST} --port ${APP_PORT}
```

### Building the Image

```sh
docker build -t my-api:v1 .
```

### Deploying to Kubernetes

If using kind locally, run this first:

```sh
kind load docker-image my-api:v1
```

Then deploy:

```sh
kubectl create deployment my-app --image=my-api:v1
```