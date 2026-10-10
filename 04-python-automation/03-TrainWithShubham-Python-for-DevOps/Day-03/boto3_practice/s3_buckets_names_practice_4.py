import boto3 

s124 = boto3.resource('s3')

def name_find(s124):
    for buckets_names in s124.buckets.all():
        print(f"Bucket = {buckets_names.name}")


name_find(s124)