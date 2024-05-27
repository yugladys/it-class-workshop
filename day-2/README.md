# Airflow Exercises

## Pre-requisites

### Download Docker Images

```sh
docker pull andrewgaul/s3proxy
docker pull mcr.microsoft.com/azure-sql-edge:latest
docker pull apache/airflow:2.8.3-python3.10
```

### Install Minikube

We will use minikube for our exercises since it can pull images from local without loading it in the cluster, and has `host.minikube.internal` DNS which we need to access running Docker containers.

```sh
brew install minikube
```

#### Starting Minikube

```sh
minikube start
eval $(minikube docker-env)
```

### Install Helm & Airflow

```sh
brew install helm
```

### Install Airflow

Build our airflow image:

```docker
docker build -t mydags:v1 -f airflow.Dockerfile .
```

Create new namespace and set context:

```sh
kubectl create ns workshop
kubectl config set-context --namespace=workshop --cluster=minikube --user=minikube workshop
kubectl config use-context workshop
```

Deploy airflow release:

```helm
export NAMESPACE=workshop
export RELEASE_NAME=workshop-release
helm upgrade $RELEASE_NAME apache-airflow/airflow --namespace $NAMESPACE \
    --set images.airflow.repository=mydags \
    --set images.airflow.tag=v1 \
    --set images.airflow.pullPolicy=Never
```

Check if airflow pods are running (make sure `READY` column has n/n containers running):

```sh
kubectl get po
```

ONLY if you are installing this days before the workshop, stop running cluster and start it again right before our workshop:

```sh
minikube stop
```

### Install Python Packages

Includes pre-requisites to for testing s3, airflow and providers.

```sh
brew install unixodbc
brew install awscli
```

```py
pip -r requirements.txt
```

If you encounter `fatal error: 'sqlfront.h' file not found` during installation of `apache-airflow-providers-microsoft-mssql`, run the following commands:

```sh
brew uninstall --force freetds
brew install freetds
brew link --force freetds
```

## Run S3 & SQL Server

```docker
docker compose up
```

## Test s3proxy connection

```sh
export AWS_ACCESS_KEY_ID=hello-access-key
export AWS_SECRET_ACCESS_KEY=hello-secret-key
aws s3api list-objects --bucket workshop --endpoint http://localhost:8083
```

OR

```py
python test_s3proxy.py
```
