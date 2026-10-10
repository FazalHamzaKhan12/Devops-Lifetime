import boto3

region = "ap-south-1"

s3 = boto3.client("s3", region_name=region)

bucket_name = "practice02-hamza-2026"

response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        "LocationConstraint": region
    }
)

print(response)