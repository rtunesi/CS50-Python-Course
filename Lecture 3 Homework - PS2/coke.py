cost = 50
allowed_coins = [5, 10, 25]

while cost > 0:
    print(f"Amount Due: {cost}")
    amount = int(input("Insert coin: "))
    if amount in allowed_coins:
        cost = cost - amount
    else:
        print("Sorry we only accept coins, please try again.")
        
change = abs(cost)
cost = 0 
print(f"Amount Due: {cost}")
print(f"Change Owed: {change}")

