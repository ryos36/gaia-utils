def select_dataframe(target_df, selected_df, key = 'source_id', debug = False):
    flag='anna_flag'
    sort_df = target_df.sort_values(key)
    sort_df[flag] = 0
    count = 0
    for i,row in selected_df.iterrows():
        if debug:
            print(row)
            print('=========')
        query_str =f'{key} == {row[key]}'
        if debug:
            print(query_str)
        hit = sort_df.query(f'{key} == {row[key]}')
        if debug:
            print(hit, hit.empty)
        if not hit.empty:
            if debug:
                print(hit)
            sort_df[flag] = 1
            count += 1
        else:
            print('Not Found!! ', key, row[key])

    anna_query_str =f'{flag} == 1'
    result_df = sort_df.query(anna_query_str)
    return result_df, count
    
# ----------------------------------------------------------------
# プログラムは段階的に作って段階的にチェックするの巻き
# ----------------------------------------------------------------
# この select_dataframe は単に target_df を
# key でソートして、anna_flag を追加した。
# 余分な anna_flag が入っている。初期値はゼロ。
# そして、selected_df から target_df のデータを探して
# フラグをたてるようにした。
# ヒットした個数を数えることにした
# データをしぼった。
# だだし、anna_flag はのこったまま
# 表示を抑制した。これでスピードは速くなるはず？
# 表示は debug モードのみとする。
# ----------------------------------------------------------------

import pandas as pd
import sys

if __name__ == '__main__':
    target_file = '../data/target.csv'
    selected_file = '../data/selected.csv'
    result_file = 'result.csv'

    target_df = pd.read_csv(target_file)
    selected_df = pd.read_csv(selected_file)

    result_df, count = select_dataframe(target_df, selected_df)

    print('count', count)
    print(target_df['source_id'][1:4])
    print(result_df['source_id'][1:4])

    result_df.to_csv(result_file)
