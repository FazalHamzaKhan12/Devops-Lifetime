import boto3
region = "us-east-1"
ec2 = boto3.client("ec2",region_name=region)


response = ec2.describe_instances()

# print(response)

# for reservation in response["Reservations"]:
#     for instance in reservation["Instances"]:
#         print(instance["InstanceId"])

print("\n")
for reservation in response["Reservations"]:
    for instance in reservation["Instances"]:
        print("Instance ID:", instance["InstanceId"])
        print("Type:", instance["InstanceType"])
        print("State:", instance["State"]["Name"])
        print("Private IP:", instance.get("PrivateIpAddress"))
        print("Public IP:", instance.get("PublicIpAddress"))
        print("--------------------")
print("\n")
print("here we go")