import boto3


region = "us-east-1"
ec2 = boto3.client("ec2",region_name=region)


response = ec2.stop_instances()(
    InstanceIds=[
        "i-02eece3f4e5220354"
    ]
)

print("Running State: ", response)


