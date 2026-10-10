import boto3

s3 = boto3.client("s3")
# s3 = boto3.resource("s3")
# both work the same but now updated is client keyword

bucket_name = "my-pyt3ndd-devops-bucket-12345"

response = s3.create_bucket(
    Bucket=bucket_name,
)

print(response)


"ATATT3xFfGF0oyJ_Vnws2l8gWXvSFKHmBNRm4HuqgAJr9HzlF8SyFdNstVUmKxKldJkFk7TsVEZaIDZUvKTtqoQLQSDpVtfe0AsJyo69ESrHBSzmplRVu9CXk6CSALqOmf8rGSjj2ABZ7_72DYQ2_3fQj6M2wNIxCV8mYRje_MS54tq0ZkxEA80=79AA1086"