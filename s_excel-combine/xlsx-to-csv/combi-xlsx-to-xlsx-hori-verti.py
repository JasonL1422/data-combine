#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep  7 01:54:29 2024
@author: jongcheollee
"""

import os
import pandas as pd

combi_type = 'vertical' ### choose 'horizontal' or 'vertical'

def combi_xlsx(concat_type = combi_type):
    folder_path = os.getcwd() 
    combined_data = pd.DataFrame() 
    xlsx_files = sorted([file for file in os.listdir(folder_path) if file.endswith('.xlsx')])
    
    for file in xlsx_files:
        file_path = os.path.join(folder_path, file)
        data = pd.read_excel(file_path)

        if concat_type == 'horizontal':
            data.columns = [f'{file}_{col}' for col in data.columns]
        else:  # default to vertical
            data.columns = [str(col).strip() for col in data.columns]
            data['Source_File'] = file

        if combined_data.empty:
            combined_data = data
        else:
            if concat_type == 'horizontal':
                combined_data = pd.concat([combined_data, data], axis=1)
            else:
                combined_data = pd.concat([combined_data, data], axis=0)
            #axis=0 vertial addition, axis=1 horizontal addition
    
    return combined_data

#------------------------------------------------------------------------------

combined_xlsx = combi_xlsx(concat_type=combi_type)
if not combined_xlsx.empty:
    combined_xlsx.to_excel(f'combined_xlsx_{combi_type}.xlsx', index=False)
    print("completed")
else:
    print("error")

