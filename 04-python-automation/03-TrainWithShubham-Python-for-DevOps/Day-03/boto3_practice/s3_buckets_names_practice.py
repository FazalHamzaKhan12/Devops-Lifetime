import boto3 

s_buckets = boto3.resource("s3")

def bucket_Names(s_buckets):
    for bucket in s_buckets.buckets.all():
        print(bucket.name)

bucket_Names(s_buckets)