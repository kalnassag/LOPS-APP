import json

from neo4j import GraphDatabase

from DataLoader import load_laptop, load_mapping
from connection import driver, AUTH, URI

# Load everything
with open('full_data/laptops.json', 'r', encoding='utf-8') as f:
    all_laptops = json.load(f)

with open('mapping_data/laptop_property_mapping.json', 'r', encoding='utf-8') as f:
    property_mapping = json.load(f)

driver = GraphDatabase.driver(URI, auth=AUTH)

try:
    print(f"Loading {len(all_laptops)} laptops...")
    for i, laptop_data in enumerate(all_laptops):
        load_laptop(driver, laptop_data, property_mapping)
        if (i + 1) % 100 == 0:
            print(f"✅ {i + 1} / {len(all_laptops)}")
    print(f"🎉 Done! Loaded {len(all_laptops)} laptops")
finally:
    driver.close()


# with open('full_data/laptops.json', 'r', encoding='utf-8') as f:
#     lines = f.readlines()
#
# # Check around the problem line
# problem_line = 193370
# print(f"Line {problem_line - 1}: {lines[problem_line - 2][:100]}")
# print(f"Line {problem_line}: {lines[problem_line - 1][:100]}")
# print(f"Line {problem_line + 1}: {lines[problem_line][:100]}")
#
# # Check the last few lines
# print("\nLast 5 lines:")
# for line in lines[-5:]:
#     print(line[:100])