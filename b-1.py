# 九九の掛け算表を出力するプログラム
for i in range(9):  # 1から9までの数値で外側のループ
    for j in range(9):  # 1から9までの数値で内側のループ
        product = (i+1) * (j+1)  # 掛け算の計算
        print(f"{product}", end=" ")  # 結果を横に並べて表示
    print()  # 各行の終わりで改行
