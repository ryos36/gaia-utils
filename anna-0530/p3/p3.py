def select_dataframe(target_df, selected_df, key = 'source_id'):
    flag='anna_flag'
    sort_df = target_df.sort_values(key)
    sort_df[flag] = 0
    for i,row in selected_df.iterrows():
        print(row)
        print('=========')
    return sort_df
    
# ----------------------------------------------------------------
# プログラムは段階的に作って段階的にチェックするの巻き
# ----------------------------------------------------------------
# この select_dataframe は単に target_df を
# key でソートして、anna_flag を追加した。
# 余分な anna_flag が入っている。初期値はゼロ。
# そして、selected_df をぐるぐる回して表示してみた。
# 表示しただけで何もしていない。
# ----------------------------------------------------------------

import pandas as pd
import sys

if __name__ == '__main__':
    target_file = '../data/target.csv'
    selected_file = '../data/selected.csv'
    result_file = 'result.csv'

    target_df = pd.read_csv(target_file)
    selected_df = pd.read_csv(selected_file)

    result_df = select_dataframe(target_df, selected_df)
    print(target_df['source_id'][1:4])
    print(result_df['source_id'][1:4])

    result_df.to_csv(result_file)
