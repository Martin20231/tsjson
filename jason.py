import json

with open ('accounts.json') as file:
    data = json.load(file)



name = input("für konto geben Sie die 1 an ")

if name == "age":
    for account in data:
        if account["age"]  > 25:
             print(account)             
elif name == "kontostand":
    balance =[]

    for i in data:
        balance.append(i["balance"])
    highest = "0"
    for number in balance:
            if number > highest:
                highest = number
    print("die höchste Zahl ist",highest)