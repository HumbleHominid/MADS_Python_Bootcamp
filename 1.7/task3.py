items: list[int] = []
while True:
    n = int(input("Enter a number: "))
    if n < 0:
        continue
    elif n == 0:
        break
    items.append(n)
