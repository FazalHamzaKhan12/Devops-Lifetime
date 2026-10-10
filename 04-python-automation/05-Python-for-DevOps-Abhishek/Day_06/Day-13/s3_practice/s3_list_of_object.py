import boto3

s3 = boto3.client('s3')

bucket_name="amaings3"

response = s3.list_objects_v2(
    Bucket=bucket_name
)

for i in response["Contents"]:
    print(i["Key"])


print(f"these are inside of your s3 {bucket_name}")

