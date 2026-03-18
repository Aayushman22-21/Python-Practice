def average():
    n = int(input("Enter the number of values: "))
    total = 0

    for i in range(n):
        value = float(input(f"Enter value {i + 1}: "))
        total += value

    avg = total / n
    print(f"The average is: {avg}")