class LaptopDataLoader:
    def __init__(self, neo4j_driver, mapping_config):
        self.driver = neo4j_driver
        self.mapping = mapping_config

    def load_laptop(self, json_data):
        """Load single laptop from JSON"""
        # 1. extract and normalise properties
        properties = self.extract_properties(json_data)

        # 2. Add boolean flags
        properties.update(self.extract_boolean_flags(json_data))

        # 3. Create/merge node in Neo4j
        self.create_laptop_node(properties)

    def extract_properties(self, data):
        """Extract all properties using mapping config"""

    properties = {}
