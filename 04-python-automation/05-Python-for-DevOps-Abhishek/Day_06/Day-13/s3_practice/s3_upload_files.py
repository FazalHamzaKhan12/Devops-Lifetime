import boto3

s3 = boto3.client("s3")

bucket_name = "amaings3"

uploading_file_loc = r"C:\Users\Fazal Hamza Khan\Downloads\DevOPS\Python FOR Devops\05-Python-for-DevOps-Abhishek\Day_06\Day-13\s3_practice\test.txt"

s3.upload_file(
    uploading_file_loc,
    bucket_name,
    "test.txt"
)

print("File uploaded successfully")