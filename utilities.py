import json, re
import pandas as pd


def normalise_path_to_properties(col, product_type=None):
    """
    Reads the JSON file and converts the dot notation (e.g. Product.Model Name) to
    an appropriate snake case property name (product_model_name).
    Replaces first-level keys (Design, Inside, Display, etc.) with the product type.

    Args:
        col: The column name in dot notation (e.g., "Design.Body.Height_mm")
        product_type: The type of product in singular form (e.g., 'laptop', 'tablet', 'smartwatch')

    Returns:
        Normalised property name with first-level key replaced by product type
        E.g., "Design.Body.Height_mm" -> "laptop_body_height_mm"
              "Inside.Software.OS" -> "smartwatch_software_os"
    """
    pattern = r'[\s().]+'
    normalised_item = re.sub(pattern, "_", str(col))
    normalised_item = re.sub(r'_+', '_', normalised_item)
    normalised_item = normalised_item.strip("_").lower()
    if normalised_item.startswith("no_"):
        normalised_item = "has" + normalised_item.lstrip("no.")

    # Replace first-level key with product type
    if product_type and '_' in normalised_item:
        # Split the normalized item to get the first segment
        parts = normalised_item.split('_')
        first_level_key = parts[0]

        # List of first-level keys that should be replaced with product type
        replaceable_keys = ['design', 'inside', 'display', 'camera', 'product']

        if first_level_key in replaceable_keys:
            # Replace the first segment with product type
            parts[0] = product_type
            normalised_item = '_'.join(parts)

    return normalised_item

def to_singular(category):
    """
    Converts a category name to singular form.
    E.g., 'Laptops' -> 'laptop', 'Tablets' -> 'tablet', 'Smartwatches' -> 'smartwatch'
    """
    if not category:
        return None
    category = category.lower()
    # Handle words ending in 'ches', 'shes', 'xes', 'ses' -> remove 'es'
    if category.endswith(('ches', 'shes', 'xes', 'ses')):
        return category[:-2]
    # Handle words ending in 's' -> remove 's'
    elif category.endswith('s'):
        return category[:-1]
    return category

def map_properties(sample_file):
    """"
    Maps property names from the json files to the normalised property name as they should appear in the graph.
    Check the files *_property_mapping.json to see how tha looks like.
    """
    property_mapping = {}
    with open(sample_file, 'r') as sf:
        file = json.load(sf)

        # Extract product type from Product.Category field
        product_category = file.get('Product', {}).get('Category', None)
        product_type = to_singular(product_category) if product_category else None

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