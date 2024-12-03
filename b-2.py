rows = int(input("行数を入力してください: "))
columns = int(input("列数を入力してください: "))

for i in range(rows):
    for j in range(columns):
        product = (i+1) * (j+1)
        print(f"{product}", end=" ")
    print()
