# Start an infinite Loop
while True:
    n = int(input("What is n?: "))
    if n > 0:
        # Break out of the loop
        break

# Print meow as many times as the user enters entered number
# i.e: n = 10 then print meow x10
# _ is used to store the last expression to a variable that won't be used again.
for _ in range(n):
    print("meow")