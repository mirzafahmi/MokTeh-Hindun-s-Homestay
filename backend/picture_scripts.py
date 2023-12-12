import os
import json

media_folder_path = os.path.join(os.path.dirname(__file__), 'media')
json_file_path = 'homestays_list.json'

with open(json_file_path, 'r') as json_file:
    houses = json.load(json_file)

for house in houses:
    house_name = house['name']
    house_folder_path = os.path.join(media_folder_path, house_name)

    house_images = [f for f in os.listdir(house_folder_path) if os.path.isfile(os.path.join(house_folder_path, f))]

    house['picture'] = [f'/media/{house_name}/{image}' for image in house_images]

with open(json_file_path, 'w') as json_file:
    json.dump(houses, json_file, indent=2)

print(houses)
