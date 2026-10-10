import boto3

s3 = boto3.client('s3')

# for bucket in s3.buckets.all():
#     if "pow" in bucket.name:
#         print(bucket.name)

filename = "C:\\Users\\Fazal Hamza Khan\\Downloads\\DevOPS\\Python FOR Devops\\02-TrainWithShubham-Python\\Day-03\\fastapi\\01_api.py"

objectname = "01_api.py"
bucket = "devops-ai-powerede"


response = s3.upload_file(filename, bucket, objectname)