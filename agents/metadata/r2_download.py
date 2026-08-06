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


def download_file(r2_key, local_file):

    os.makedirs(
        os.path.dirname(local_file),
        exist_ok=True
    )

    client.download_file(
        os.getenv("R2_BUCKET"),
        r2_key,
        local_file
    )

    print(
        f"Downloaded {r2_key} -> {local_file}"
    )


if __name__ == "__main__":

    download_file(
        "images/4.jpg",
        "tmp/test.jpg"
    )