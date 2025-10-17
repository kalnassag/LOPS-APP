import json, re
import pandas as pd


def normalise_path_to_properties(col):
    """
    Reads the JSON file and converts the dot notation (e.g. Product.Model Name) to
    an appropriate snake case property name (product_model_name)
    """
    pattern = r'[\s().]+'
    normalised_item = re.sub(pattern, "_", str(col))
    normalised_item = re.sub(r'_+', '_', normalised_item)
    normalised_item = normalised_item.strip("_").lower()
    if normalised_item.startswith("no_"):
        normalised_item = "has" + normalised_item.lstrip("no.")
    return normalised_item

def map_properties(sample_file):
    """"
    Maps property names from the json files to the normalised property name as they should appear in the graph.
    Check the files *_property_mapping.json to see how tha looks like.
    """
    property_mapping = {}
    with open(sample_file, 'r') as sf:
        file = json.load(sf)
        data = pd.json_normalize(file)
        for col in data.columns:
            if col.startswith('No.'):
                continue
            graph_property = normalise_path_to_properties(col)
            property_mapping[col] = graph_property
    return property_mapping

def save_mapping(prop_mapping, filename='laptop_property_mapping.json'):
    with open(filename, 'w') as f:
        json.dump(prop_mapping, f, indent=2)
        print("succeeded")

save_mapping(map_properties('smartwatch_property_mapping.json'), filename = 'smartwatch_property_mapping.json')