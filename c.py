class Customer:
    # 各問のコードが期待通り動作するように実装
    def __init__(self, first_name, family_name, age):
        self.first_name = first_name
        self.family_name = family_name
        self.age = age

    def full_name(self):
        return self.first_name + " " + self.family_name

    def entry_fee(self):
        if self.age <= 3:
            return 0
        elif self.age < 20:
            return 1000
        elif self.age >= 20 and self.age < 65:
            return 1500
        elif self.age >= 75:
            return 500
        else:
            return 1200

    def info_csv(self):
        return f"{self.full_name()},{self.age},{self.entry_fee()}"

    def info_tab(self):
        return f"{self.full_name()}\t{self.age}\t{self.entry_fee()}"

    def info_pipe(self):
        return f"{self.full_name()}|{self.age}|{self.entry_fee()}"


ken = Customer(first_name="Ken", family_name="Tanaka", age=15)
tom = Customer(first_name="Tom", family_name="Ford", age=57)
ieyasu = Customer(first_name="Ieyasu", family_name="Tokugawa", age=73)
michelle = Customer(first_name="Michelle", family_name="Tanner", age=3)


print(ken.full_name())
print(tom.full_name())

print(ken.age)
print(tom.age)
print(ieyasu.age)

print(ken.entry_fee())
print(tom.entry_fee())
print(ieyasu.entry_fee())
print(michelle.entry_fee())

print(ken.info_csv())
print(tom.info_csv())
print(ieyasu.info_csv())
print(michelle.info_csv())


print(ken.info_tab())
print(tom.info_tab())
print(ieyasu.info_tab())
print(michelle.info_tab())

print(ken.info_pipe())
print(tom.info_pipe())
print(ieyasu.info_pipe())
print(michelle.info_pipe())
