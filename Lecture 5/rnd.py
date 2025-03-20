import random as rd

count = 0
head_count = 0
tail_count = 0
while count != 100:
    coin = rd.choice(["Head", "Tails"])
    print(coin)
    if coin == "Tails":
        tail_count += 1
    else:
        head_count +=1
    count += 1

print(head_count)
print(tail_count)
