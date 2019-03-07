import json

with open ('./www/colors.json') as color_json:
    color_json_dumped = json.load(color_json)
print (color_json_dumped)
