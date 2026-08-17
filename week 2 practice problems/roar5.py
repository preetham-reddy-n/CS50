i = int(input("How many times do you want to roar? "))

while True:
    if i>0:
        break
    else:
        i = int(input("Invalid input, enter again.  "))

for _ in range(i):
    print("Roar")