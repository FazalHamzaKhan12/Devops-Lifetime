import boto3

s5 = boto3.resource("s3")


def bucket_n_finder(s5):
    for buckets in s5.buckets.all():
        print(buckets.name)


bucket_n_finder(s5)