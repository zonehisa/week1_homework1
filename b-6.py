import random

dice_face = input("サイコロの面の数は？ >")
dice_count = input("サイコロを何回振りますか？ >")

result = []
for i in range(int(dice_count)):
    result.append(random.randint(1, int(dice_face)))
print(result)
