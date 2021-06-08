#!/usr/bin/env python3

import pandas as pd
import sys
from gaia_utils import select_dataframe 
 
target_file = '../anna-0530/data/target.csv'
selected_file = 'gaia_id.csv'
result_file = 'gaia_result.csv'

target_df = pd.read_csv(target_file, sep=',')
selected_df = pd.read_csv(selected_file, sep=',')

result_df, count = select_dataframe(target_df, selected_df, key_selected = 'gaia_id')

print('count', count)

result_df.to_csv(result_file, index=False)

