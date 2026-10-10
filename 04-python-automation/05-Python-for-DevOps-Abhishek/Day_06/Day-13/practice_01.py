import boto3

s3 = boto3.client("s3")

bucket_name = "my-pythondd-devops-bucket-12345"

response = s3.get_bucket_acl(
    Bucket=bucket_name,
)

print(response)