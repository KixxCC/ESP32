import json

with open ('./www/examples/color_set.json') as color_json:
    color_json_dumped = json.load(color_json)
with open('./www/colors.json') as colors_json:
    colors_raw = json.load(colors_json)
all_colors_json = colors_raw['defaults'].copy()
all_colors_json.update(colors_raw['user_set'])
name,color = color_json_dumped['name'],color_json_dumped['color']

if name in all_colors_json.keys():
        color_name_exists = all_colors_json[name]
        print("moom")
elif color in all_colors_json.values():
        color_name = all_colors_json.keys()[all_colors_json.values().index(color)]
        print("mood")
        #send color already exists error with name
else:
    print(all_colors_json[name])