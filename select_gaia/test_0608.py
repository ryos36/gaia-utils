#!/usr/bin/env python3

import pandas as pd
import sys
from gaia_utils import select_dataframe 
    
if __name__ == '__main__':
    alen = len(sys.argv)
    if ( alen != 3 ) and ( alen != 4 ):

        print(f'Usage:{sys.argv[0]} target.csv selected.csv [result.csv]', file=sys.stderr);
        print(f'   please try:{sys.argv[0]} ../anna-0530/data/target.csv ../anna-0530/data/selected2.csv')
        sys.exit(255)
    
    target_file = sys.argv[1]
    selected_file = sys.argv[2]
    result_file = sys.argv[3] if alen == 4 else 'result.csv'

    target_df = pd.read_csv(target_file, sep=',')
    selected_df = pd.read_csv(selected_file, sep=',')

    result_df, count = select_dataframe(target_df, selected_df)

    print('count', count)
    print(target_df['source_id'][1:4])
    print(result_df['source_id'][1:4])

    result_df.to_csv(result_file, index=False)

