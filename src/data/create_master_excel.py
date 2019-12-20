# import statements
import pandas as pd
import numpy as np
import os

### functions ###

# create function to pull first four characters of column
def str_4 (x):
	return x.str[:4]

# create function to compare lists and assign to var
def intersection (i):
	return x_i = set(passi['hist4']).intersection(icd032['hist'])

# create function to match if is in list and assign 'Y'
def match (m):
	return m.loc[m['hist4'].isin(x_m), 'ICD03.2'] = 'Y'
	pass

# create function to ouput finalized sheet
def out (o):
	return o_out.to_excel('dir/o.xlsx', sheet_name='o', index=False)

### reference ###

# create reference lists
# icd032
icd032 = pd.read_excel(pass,sheet_name='pass')
icd032['hist'] = str_4(icd032['ICD03.2'])

#c15['hist4'] = c15['Histology'].str[:4]

#x15 = set(c15['hist4']).intersection(icd032['hist'])

## assign Y if match
#c15.loc[c15['hist4'].isin(x15), 'ICD03.2'] = 'Y'

## drop histology column
#c15_out = c15.drop(columns=['hist4'])

# ### output
#c15_out.to_excel('H:/DQAIB/tara_histology_project/tara_ajcchist_outputs3/c15.xlsx', sheet_name="C15", index=False)
