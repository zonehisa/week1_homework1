def get_input():
    """ユーザーから行数と列数を入力を受け取る"""
    rows = int(input("行数を入力してください: "))
    columns = int(input("列数を入力してください: "))
    return rows, columns


def print_multiplication_cell(row, column):
    """掛け算の1セルを出力する"""
    product = row * column
    print(f" {row} × {column} = {product:2} ", end="|")


def print_multiplication_table():
    """掛け算表を出力する"""
    rows, columns = get_input()

    for i in range(rows):
        row = i + 1
        for j in range(columns):
            column = j + 1
            print_multiplication_cell(row, column)
        print()


print_multiplication_table()
