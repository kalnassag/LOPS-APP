import json
import re
from os.path import split

import pandas as pd

property_mapping = {}

# def json_mapping(file):
#     # with open(file, 'r') as file:
#     print(pd.json_normalize(file))
#
# json_mapping('sample.json')
f = open('sample.json', 'r')
file = json.loads(f.read())

print (type(file))

print(file.keys())
print(file['Design'].keys())
print(file['Design']['Keyboard'].keys())
print(file['Design']['Keyboard']['Additional Features'])

data = pd.json_normalize(file)
pattern = r'[\s().]+'

for item in data:
    normalised_item = re.sub(pattern, "_", str(item))
    print(f"\"{item}\": \"{normalised_item}\",")