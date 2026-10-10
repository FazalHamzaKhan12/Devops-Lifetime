import boto3

s3 = boto3.client("s3")
bucket_name = "amaings3"

s3.download_file(
    bucket_name,
    "test.txt", # file on s3
    "downloaded_test.txt" # where /name to save on your pc

)

print("File downloaded Successfully")