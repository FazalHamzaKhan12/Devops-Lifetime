import boto3

region = "us-east-1"

ec2 = boto3.client("ec2", region_name=region)

response = ec2.run_instances(
    ImageId="ami-0b6d9d3d33ba97d99",
    InstanceType="t2.micro",
    MinCount=1,
    MaxCount=1,

    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [
                {
                    "Key": "Name",
                    "Value": "My-DevOps-Server"
                }
            ]
        }
    ]
)

print(response)