次の戦略でプログラムを作る

デカい方のデータを Pandas で読みデータフレーム(df0) にする。
df0 を SOURCE_ID でソートする
df0 に column を追加。anna_flag とする。初期値は０
小さいほうのデータを Pandas で読み df1 とする。
すべての df1 のデータを for 文で回し、、、、
df1 の SOURCE_ID から df1 の row を探す。
あれば、その row の anna_flag を 1 にする。
なければ、ねぇ〜よと一応ワーニングをプリントする。
全部の df1 のデータを見終わると df0 の anna_flag に df1 にあったデータには 1 がたっている。
df0 で query で anna_flag == 1 のものを選択しそれを result_df とする
anna_flag の column を削除する。
result_df を to_csv でセーブする。
