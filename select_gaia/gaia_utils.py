#!/usr/bin/env python3

def select_dataframe(target_df, selected_df, key_target = 'source_id', key_selected = 'source_id'):

    lst=[]

    for gaiaID in selected_df[key_selected]:
        match_indexes = target_df[target_df[key_target] == gaiaID].index

        #
        # if len(match_indexes) != 1:
        #    print(gaiaID)
        #

        data = target_df.loc[match_indexes,:]
        lst.append(data)

    return pd.concat(lst), len(lst)

import pandas as pd
import sys
    
if __name__ == '__main__':
    alen = len(sys.argv)
    if ( alen != 3 ) and ( alen != 4 ):
        print(f'Usage:{sys.argv[0]} target.csv selected.csv [result.csv]', file=sys.stderr);
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

