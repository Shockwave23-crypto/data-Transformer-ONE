import os
import random
import string
os.system("cls")
print(f" {'Transformers ONE':-^10}")
data = dict()
while True:
    Key = "".join(random.choice(string.ascii_uppercase) for i in range(3))
    print(f"Key = {Key}")
    Name = input("Enter Name\t:")
    Faction = input("Enter Faction\t:")
    Altmode   = input("Enter Altmode\t:")
    option = input("input your data again (y/n) :").lower()
    data[Key] = {"Name": Name, "Faction": Faction, "Altmode": Altmode }
    if option == "n":
        break
    elif option == "y":
        continue


print("_"*40)
print(f"key\t Enter Name\t Enter Faction\t Enter Altmode")
print("_"*40)
for k, v in data.items():
    print(f"{Key}.\t {data[Key][ "Name" ]}\t {data[Key][ "Faction" ]}\t \t{data[Key]["Altmode"]}")