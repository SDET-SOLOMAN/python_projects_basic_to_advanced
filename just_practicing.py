def diamond(n):
    if n % 2 != 0 and n > 0:
        my_diamond = ""
        for num in range(1, n + 1):
            if num % 2 != 0:
                my_diamond += "*" * num
                my_diamond += "\n"
        for num in range(n - 1, 0, -1):
            if num % 2 != 0:
                my_diamond += "*" * num
                my_diamond += "\n"
        return my_diamond
    return None


print(diamond(5))

for num in range(1, 8 + 1):
    if num % 2 != 0:
        print(" " * (8 - num) + "*" * num + "\n")