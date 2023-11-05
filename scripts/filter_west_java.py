import json

with open('data/indonesia_villages_border.geojson', 'r') as file:
    data = json.load(file)

filtered_data = [feature for feature in data if feature['province'] == 'JAWA BARAT']

with open('data/indonesia_villages_jawa_barat.geojson', 'w') as file:
    json.dump(filtered_data, file)

print(f"Filtered {len(filtered_data)} features for JAWA BARAT province.")