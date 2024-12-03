input_data = input("データを入力してください(スペース区切り) >")
data_list = input_data.split()


def calc_total(data_list):
    total = 0
    for data in data_list:
        total += int(data)
    return total


def max_value(data_list):
    # 空のリストの場合はNoneを返す
    if not data_list:
        return None
    # 最初の要素を初期値とする
    value = int(data_list[0])
    for data in data_list:
        if value < int(data):
            value = int(data)
    return value


def min_value(data_list):
    if not data_list:
        return None
    value = int(data_list[0])
    for data in data_list[1:]:
        if value > int(data):
            value = int(data)
    return value


def average_value(data_list):
    return int(calc_total(data_list) / len(data_list))


print("合計値:", calc_total(data_list))
print("最大値:", max_value(data_list))
print("最小値:", min_value(data_list))
print("平均値:", average_value(data_list))
