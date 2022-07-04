import json
with open("10506.json", "r", encoding="UTF-8") as fp:
    jsondata = fp.read()
data = json.loads(jsondata)
data = data['responseData']
for item in data:
    print(item['family_name'], item['gender'], item['people_total'])
