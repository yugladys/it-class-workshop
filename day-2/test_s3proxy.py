import logging
import boto3
from botocore.exceptions import ClientError


def create_bucket(bucket_name):

    try:
        s3_client = boto3.client("s3", 
                                 endpoint_url="http://localhost:8083", 
                                 aws_access_key_id="hello-access-key", 
                                 aws_secret_access_key="hello-secret-key"
                                 )
        s3_client.create_bucket(Bucket=bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True

create_bucket("test-s3proxy")