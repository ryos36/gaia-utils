def select_dataframe_v0(target_df, selected_df, key = 'SOURCE_ID'):
    result_df = target_df
    return result_df
    
# ----------------------------------------------------------------
# プログラムは段階的に作って段階的にチェックするの巻き
# ----------------------------------------------------------------
# この select_dataframe_v0 はなにもしない。たんに target_df を
# そのまま返しているだけ。コピーすらしていない
# __main__ のチェックになる。
# ----------------------------------------------------------------

import pandas as pd
import sys

if __name__ == '__main__':
    target_file = '../data/target.csv'
    selected_file = '../data/selected.csv'
    result_file = 'result.csv'

    target_df = pd.read_csv(target_file)
    selected_df = pd.read_csv(selected_file)

    result_df = select_dataframe_v0(target_df, selected_df)

    result_df.to_csv(result_file)
