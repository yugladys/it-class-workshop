# Airflow Exercises

## *PRE-REQUISITES*

### Install Python Packages

```sh
brew install unixodbc
brew install awscli
```

```sh
cd day-2
```

```py
pip install -r requirements.txt
```

If you encounter `fatal error: 'sqlfront.h' file not found` during installation of `apache-airflow-providers-microsoft-mssql`, run the following commands:

```sh
brew uninstall --force freetds
brew install freetds
brew link --force freetds
```

### Download Docker Images

```sh
docker pull andrewgaul/s3proxy
docker pull mcr.microsoft.com/azure-sql-edge:latest
docker pull apache/airflow:2.8.3-python3.10
```

### Install Airflow on Minikube

We will use minikube for our exercises since it can pull images from local without loading it in the cluster, and has `host.minikube.internal` DNS which we need to access running Docker containers.

```sh
brew install minikube
brew install helm
```

Starting Minikube:

```sh
minikube start
```

### Install Airflow

Build airflow image (make sure to run minikube eval in the same terminal as docker build):

```docker
eval $(minikube docker-env)
docker build -t mydags:v1 -f airflow.Dockerfile .
```

Create your own namespace and set the proper context using kubectl config. 
*(You can go back to Day 1 slides on how to do this)*

Install the helm chart for apache airflow:
```helm
helm repo add apache-airflow https://airflow.apache.org
```

Deploy airflow release using helm:
```helm
export NAMESPACE=<your namespace>
export RELEASE_NAME=workshop-release
helm install $RELEASE_NAME apache-airflow/airflow --namespace $NAMESPACE \
    --set images.airflow.repository=mydags \
    --set images.airflow.tag=v1 \
    --set images.airflow.pullPolicy=Never
```

Check if airflow pods are running (make sure `READY` column has n/n containers running)*:

```sh
kubectl get po
```

ONLY if you are installing this days before the workshop, stop running cluster and start it again right before our workshop:

```sh
minikube stop
```

* *If you encounter the Init:ErrImageNeverPull for the airflow pods please run the following:*

```helm
minikube image load mydags:v1
helm install $RELEASE_NAME apache-airflow/airflow --namespace $NAMESPACE \
    --set images.airflow.repository=mydags \
    --set images.airflow.tag=v1 \
    --set images.airflow.pullPolicy=Never
```

## *END OF PRE-REQUISITES. SEE YOU AT THE WORKSHOP!! :)*

===================================================================================

## Run S3 & SQL Server

Docker compose file will be created as an exercise.

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
