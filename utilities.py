import json, re
import pandas as pd


def normalise_path_to_properties(col, product_type=None):
    """
    Reads the JSON file and converts the dot notation (e.g. Product.Model Name) to
    an appropriate snake case property name (product_model_name).
    Removes redundant prefixes like 'design_body_' and replaces them with the product type.

    Args:
        col: The column name in dot notation
        product_type: The type of product (e.g., 'laptop', 'tablet', 'smartwatch')

    Returns:
        Normalised property name with redundant text removed and product type added where appropriate
    """
    pattern = r'[\s().]+'
    normalised_item = re.sub(pattern, "_", str(col))
    normalised_item = re.sub(r'_+', '_', normalised_item)
    normalised_item = normalised_item.strip("_").lower()
    if normalised_item.startswith("no_"):
        normalised_item = "has" + normalised_item.lstrip("no.")

    # Remove redundant prefixes and replace with product type
    if product_type:
        redundant_prefixes = [
            "design_body_",
        ]
        for prefix in redundant_prefixes:
            if normalised_item.startswith(prefix):
                # Remove the redundant prefix and add product type
                normalised_item = product_type + "_" + normalised_item[len(prefix):]
                break

    return normalised_item

def map_properties(sample_file):
    """"
    Maps property names from the json files to the normalised property name as they should appear in the graph.
    Check the files *_property_mapping.json to see how tha looks like.
    """
    # Extract product type from filename (e.g., 'laptop' from 'laptop_sample.json')
    import os
    filename = os.path.basename(sample_file)
    product_type = filename.split('_')[0] if '_' in filename else None

    property_mapping = {}
    with open(sample_file, 'r') as sf:
        file = json.load(sf)
        data = pd.json_normalize(file)
        for col in data.columns:
            if col.startswith('No.'):
                continue
            graph_property = normalise_path_to_properties(col, product_type)
            property_mapping[col] = graph_property
    return property_mapping

def save_mapping(prop_mapping, filename):
    with open(filename, 'w') as f:
        json.dump(prop_mapping, f, indent=2)
        print(f"Successfully saved {filename}")

# Regenerate property mappings for all product types
save_mapping(map_properties('laptop_sample.json'), filename='laptop_property_mapping.json')
save_mapping(map_properties('tablets_sample.json'), filename='tablets_property_mapping.json')
save_mapping(map_properties('smartwatch_sample.json'), filename='smartwatch_property_mapping.json')