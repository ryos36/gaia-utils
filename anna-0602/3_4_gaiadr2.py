import pandas as pd
import numpy as np 
df1=pd.read_csv('catalog-xu2021.csv', sep=',')
df2=pd.read_csv('gaia_dr2_white_dwarf_candidates_v2.csv', sep=',')
#print(df1['gaiaID'])
#print(df2['source_id'])
df = pd.DataFrame([])  
for gaiaID in df1['gaiaID']:
    match = df2[df2['source_id'] == int(gaiaID) ].index
    #if len(match) != 1:
        #print(gaiaID)
    data=df2.loc[match,:]
    df=df.append(data)
   
​
​
df.to_csv('crsmtach_Xu_Fusillo.csv', index=False)
