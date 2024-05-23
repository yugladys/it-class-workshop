# Airflow Exercises

## Run S3

```docker
docker run -v $(PWD)/data:/data --env-file s3.env --name s3 -p 8083:8083 andrewgaul/s3proxy
```

## Run SQL Server

```docker
docker run --rm --env-file sql.env --name sql -p 1433:1433 mcr.microsoft.com/azure-sql-edge:latest
```

## Test s3proxy connection

Need to install awscli: `brew install awscli`

```sh
export AWS_ACCESS_KEY_ID=hello-access-key
export AWS_SECRET_ACCESS_KEY=hello-secret-key
aws s3api list-objects --bucket workshop --endpoint http://localhost:8083
```

OR

```py
python test_s3proxy.py
```

## TO-DO

- Maybe convert to docker runs to docker-compose
- Create csv file and sql tables using script??
- Try with airflow operators
- Do we want to add spark????
