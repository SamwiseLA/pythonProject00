import random

n = 1
while n != 0:
    i = input("Enter Num to Randomize, blank: Last Num, 0: to quit: ")
    if i == "":
        i = str(n)
    n = int(i)
    if i != "0":
        print(f"Randomize: {n} : {random.randint(1, n)}")
print("-- Good Bye ---")
