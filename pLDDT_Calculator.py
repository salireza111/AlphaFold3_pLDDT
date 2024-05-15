"""
@author: alireza

place this file on AlphaFold3 predicted directory
In case of using AlphaFold2 replace ('atom_plddts') with ('plddt') in line 12
"""

import json
import os
import numpy as np
#In case of using AlphaFold2 replace ('atom_plddts') with ('plddt') 
FindFor = 'atom_plddts'


def find_json_files(directory):
    json_files = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.json'):
                json_files.append(os.path.join(root, file))
                
    return json_files

files = find_json_files('/Users/alireza/Desktop/Works/Zist Rayanesh/H1129/AF3/fold_h1129-2')
for file in files:
    with open(file) as f:
        d = json.load(f)
        if FindFor in d:
            avg =  np.array(d[FindFor]).mean() 
            print(file,'Average pLDDT: ',avg)