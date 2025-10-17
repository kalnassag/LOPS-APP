import json, re
import pandas as pd


def normalise_path_to_properties(col):
    pattern = r'[\s().]+'
    normalised_item = re.sub(pattern, "_", str(col))
    normalised_item = re.sub(r'_+', '_', normalised_item)
    normalised_item = normalised_item.strip("_").lower()
    if normalised_item.startswith("no_"):
        normalised_item = "has" + normalised_item.lstrip("no.")
    return normalised_item

def map_properties():
    property_mapping = {}
    with open('smartwatch_sample.json', 'r') as f:
        file = json.load(f)
        data = pd.json_normalize(file)
        for col in data.columns:
            if col.startswith('No.'):
                continue
            graph_property = normalise_path_to_properties(col)
            property_mapping[col] = graph_property
    return property_mapping

prop_mapping = map_properties()

def save_mapping(prop_mapping, filename='laptop_property_mapping.json'):
    with open(filename, 'w') as f:
        json.dump(prop_mapping, f, indent=2)
        print("succeeded")

save_mapping(prop_mapping, filename = 'smartwatch_property_mapping.json')