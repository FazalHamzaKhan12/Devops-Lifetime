# list, dict , and set - the collections you'll use all the time.
print("\n\n")

clouds = ["aws", "azure", "gcp"]
print(f"clouds: {clouds}")
print(type(clouds))
clouds.append("oracle")
print(f"clouds: {clouds}")
print(f"clouds[0]: {clouds[0]}")
print(f"clouds[1]: {clouds[1]}")
print(f"clouds[2]: {clouds[2]}")
print(f"clouds[3]: {clouds[3]}")
print(f"clouds[-1]: {clouds[-1]}")
print("length        :", len(clouds))
print("count of aws  :", clouds.count("aws"))
print("index of gcp  :", clouds.index("gcp"))
print("sliced clouds :", clouds[1:3])
print("sliced clouds :", clouds[1:])
print("sliced clouds :", clouds[:3])
print("sliced clouds :", clouds[:])
print("\n\n")


for cloud in clouds:
    marker = "(market leader)" if cloud == "aws" else "(not market leader)"
    print(f"{cloud.upper()}{marker}")
    print(f"  - {cloud} {marker}".rstrip())


info = {
    "name" : "fazalhamza",
    "city" : "karachi",
    "favvoritethings" : ["Devops", "learningnew"]
}

print("\ncity       : ", info["city"])
# .get() returns a default instead of crashing when a key is missing.
print("favoirutes: ",info.get("favvoritethings", "not found"))
print("favoirutes    :", info.get("favvoritethings", "Not Found"))
print("missing key   :", info.get("hobbies", "Not Found"))

info.update({"channel": "trainwithshubman"})

for key, value in info.items():
    print(f"  {key}: {value}")

print(type(info))

nums = {1,2,3,4,5,6,6,7,8}
unique = sorted(set(nums))
print("\n unique nums: ", unique)
print(type(nums))
