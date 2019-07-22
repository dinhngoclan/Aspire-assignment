# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import json 
import pandas as pd 
from pandas.io.json import json_normalize #package for flattening json in pandas df


def test_iterate(df, pid):
    global category
    temp = df[['category_id', 'var', 'leaf', 'name']]
    temp['pid'] = pid
    category = category.append(temp)
    try:
        df["children"].apply(lambda x: test_iterate(pd.DataFrame(x), temp['category_id'][0]) if type(x) is list  else [])
    except Exception as inst:
        print(inst)
        pass

#load json object
with open("C:/Users/PC/Downloads/categories_product.json", encoding='utf-8') as f:
    d = json.load(f)

#lets put the data into a pandas df
#clicking on raw_nyc_phil.json under "Input Files"
#tells us parent node is 'programs'
category_tree = json_normalize(d["category-tree"])
category = pd.DataFrame()
test_iterate(category_tree,0)


