for num in range(1, 5):
    print(num, end="")
    if num % 2 == 0:
        print("〇", end="-")
        continue
    print("×", end="-")
