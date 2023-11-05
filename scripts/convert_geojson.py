
import json
import sys

input_file_path = sys.argv[1]

output_file_path = sys.argv[2]

# Function to convert the GeoJSON data
def convert_geojson(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    feature_collection = {
        "type": "FeatureCollection",
        "features": []
    }

    for entry in data:
        feature = {
            "type": "Feature",
            "properties": {
                "province": entry["province"],
                "district": entry["district"],
                "sub_district": entry["sub_district"],
                "village": entry["village"]
            },
            "geometry": {
                "type": "Polygon",
                "coordinates": [entry["border"]]
            }
        }
        feature_collection["features"].append(feature)

    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(feature_collection, file, ensure_ascii=False, indent=4)

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python convert_geojson.py input_file_path output_file_path")
        sys.exit(1)

    convert_geojson(input_file_path, output_file_path)

# This script requires two arguments: the input file path and the output file path.
# It can be run from the command line as follows:
# python convert_geojson.py input.geojson output.geojson
