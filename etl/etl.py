import os
import boto3
import pandas as pd

bucket = os.getenv("BUCKET_NAME")
endpoint = os.getenv("AWS_ENDPOINT_URL")

s3 = boto3.client(
    "s3",
    endpoint_url=endpoint,
    aws_access_key_id="test",
    aws_secret_access_key="test",
    region_name="us-east-1"
)

# Download input file
s3.download_file(bucket, "raw/input.csv", "/tmp/input.csv")

df = pd.read_csv("/tmp/input.csv")

# Transform
df = df[df["value"] > 10]
df["double_value"] = df["value"] * 2

df.to_csv("/tmp/output.csv", index=False)

# Upload processed file
s3.upload_file("/tmp/output.csv", bucket, "processed/output.csv")

print("ETL Completed Successfully")