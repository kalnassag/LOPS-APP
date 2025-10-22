import json
from data_extraction import get_nested_value, normalise_value, extrac_boolean_flags

def load_mapping(mapping_file):
    with open(mapping_file, 'r', encoding='utf-8') as f:
        return json.load(f)

def create_node(driver, properties):
    # Ensure _id exists
    if '_id' not in properties:
        raise ValueError("Missing required fields: _id")
    query = """
    MERGE (l:Laptop {_id: $id})
    SET l += $props
    RETURN l
    """
    with driver.session() as session:
        result = session.run(
            query,
            id=properties['_id'],
            props=properties
        )
        return result.single()


def load_laptop(driver, json_data, property_mapping):
    # 1. Extract regular properties using mapping
    properties = {}
    for json_path, graph_property in property_mapping.items():
        value = get_nested_value(json_data, json_path)
        if value is not None:
            normalised = normalise_value(graph_property, value)
            if normalised is not None:
                properties[graph_property] = normalised

    # # DEBUG: Check what we get
    # print("Properties extracted: ", len(properties))
    # print("_id in properties?", "_id" in properties)
    # print("Properties keys:", list(properties.keys())[:10])

    # 2. Add boolean flags
    flags = extrac_boolean_flags(json_data)
    properties.update(flags)

    # 3. create node in Neo4j
    create_node(driver, properties)
