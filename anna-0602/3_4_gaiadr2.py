import pandas as pd
import numpy as np 

target_file = '../anna-0530/data/target.csv'
key1='source_id'
#selected_file = '../anna-0530/data/selected2.csv'
selected_file = '../anna-0530/data/target.csv'
#key2='gaiaID'
key2='source_id'
result_file = 'result.csv'

df1=pd.read_csv(target_file, sep=',')
#df2=pd.read_csv(selected_file, sep=',').sort_values(key2)
df2=pd.read_csv(selected_file, sep=',')

#print(df1['gaiaID'])
#print(df2['source_id'])

lst=[]
for gaiaID in df1[key2]:
    match = df2[df2[key1] == int(gaiaID) ].index
    #if len(match) != 1:
        #print(gaiaID)
    data=df2.loc[match,:]
    lst.append(data)
df = pd.concat(lst)

df.to_csv(result_file, index=False)
