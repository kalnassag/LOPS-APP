import json
import re

from data_mapper import normalise_path_to_properties

def get_nested_value(data, path):
    keys = path.split('.')
    result = data
    for key in keys:
        # Check if result is a dictionary and has the key
        if isinstance(result, dict) and key in result:
            result = result[key]
        else:
            # Key doesn't exist, return None
            return None
    return result

def extrac_boolean_flags(data):
    # Get the "No" section (empty dict if it doesn't exist)
    no_section = data.get('No', {})
    # Start with an empty result
    flags = {}

    # For each feature in the "No" section
    for feature in no_section.keys():
        # Convert "Touchscreen" → "has_touchscreen"
        # Reuse the existing normalisation function
        path = f"No.{feature}"
        property_name = normalise_path_to_properties(path)

        # It's in the "No" section, so it's absent (False)
        flags[property_name] = False

    return flags

# Patterns that indicate numeric fields
numeric_keywords = ['number_of', 'speed', 'cache', 'capacity',
                    'frequency', 'version', 'ports']

def normalise_value(property_name, value):
    # Handle None, or empty
    if value is None or value == "" :
        return None

    # Check property name patterns
    if property_name.endswith(('_mm', '_g', '_wh')) or  any(keyword in property_name for keyword in numeric_keywords):
        # Convert to number
        num_string = extract_number(value)
        if num_string is None:
            return None
        return convert_to_number(num_string)

    elif property_name.startswith('has_'):
        # Already boolean, just return
        return bool(value)
    else:
        # Keep as string
        return str(value)

def is_numeric(value):
    """Check if the value is numeric to ensure we store it with the proper format"""
    try:
        float(value)
        return True
    except (ValueError, TypeError):
        return False


def extract_number(value):
    """Extract numbers from combined text values like 4.3 Ghz or 120 hz"""
    match = re.search(r'[\d.]+', str(value))
    if match:
        return match.group()
    return None

def convert_to_number(value):
    num = float(value)

    if num.is_integer():
        return int(num)
    else:
        return num