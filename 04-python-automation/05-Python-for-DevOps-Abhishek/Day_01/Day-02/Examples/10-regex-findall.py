# import re

# text = "the brown fox"
# patten = r"brown"

# serach = re.search(patten,text)

# if serach:
#     print("Pattern Found: ", serach.group())
# else:
#     print("Pattern not found")



import re

text = "quick brown fox"
pattern = r"quick"

match = re.match(pattern, text)
if match:
    print("Match found:", match.group())
else:
    print("No match")

    