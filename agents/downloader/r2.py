import os
import boto3
from dotenv import load_dotenv

load_dotenv()

client = boto3.client(
    "s3",
    endpoint_url=os.getenv("R2_ENDPOINT"),
    aws_access_key_id=os.getenv("R2_ACCESS_KEY"),
    aws_secret_access_key=os.getenv("R2_SECRET_KEY"),
)

def upload_file(local_file, remote_file):

    client.upload_file(
        local_file,
        os.getenv("R2_BUCKET"),
        remote_file
    )

    print(f"Uploaded: {remote_file}")