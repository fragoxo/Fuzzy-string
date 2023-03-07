from fuzzywuzzy import fuzz # Fuzzy string matching
import pandas as pd
import json
import requests

#  Create the promt
response = requests.get("https://master--chevignon.myvtex.com/api/catalog_system/pub/products/search/?_from=1&_to=50")
df = pd.DataFrame(response.json())
dict_products = df.iloc[:12].to_dict(orient='records')
data = {}
data['keyword'] = name = input("Enter the keyword: ") # Enter the keyword
data['productos'] = dict_products

# Calculate the score
for i, products in enumerate(data['productos']):
    data['productos'][i]['score'] = fuzz.ratio(data['keyword'], products['productName'])

# Write the results
with open("response.json", "w") as outfile:
    json.dump(data, outfile)