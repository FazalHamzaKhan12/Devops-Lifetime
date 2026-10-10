import boto3 

s3 = boto3.resource("s3")

def bucket_name_find(s3):
    for bucket in s3.buckets.all():
        print(bucket.name)


bucket_name_find(s3)