print("1.")
rows = 5
cols = 4

for i in range(rows):
    for j in range(cols):
        print("*", end="")
    print()

print("2.")
n = 6

for i in range(n):
    for j in range(n):
        if i == 0 or i == n - 1 or j == 0 or j == n - 1:
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("3.")
n = 6

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")
    print("*" * (2 * i - 1))

print("4.")
n = 6

for i in range(1, n + 1):
    print(" " * (n - i) + "*" * i)

print("5.")
n = 6

for i in range(1, n + 1):
    print(" " * (n - i), end="")
    print("* " * i)

print("6.")
n = 6

for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if i == n or j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()
print("7.")
n = 6

# Upper half
for i in range(1, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(n - 1, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("8.")
n = 4

for i in range(1, n + 1):
    print("* " * i)

for i in range(n - 1, 0, -1):
    print("* " * i)

print("9.")
n = 6

# Upper half
for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if i == n or i == 1 or j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

# Lower half
for i in range(2, n + 1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if i == n or j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("10.")
n = 11

for i in range(1, n + 1):
    for j in range(1, n + 1):

        if (i == 1 or i == n or
            j == 1 or j == n or
            i == j or
            i + j == n + 1 or
            i == (n + 1) // 2 or
            j == (n + 1) // 2):
            print("*", end=" ")
        else:
            print(" ", end=" ")

    print()

print("11.")
n = 6

for i in range(n, 0, -1):
    print(" " * (n - i), end="")

    for j in range(1, 2 * i):
        if i == n or j == 1 or j == (2 * i - 1):
            print("*", end="")
        else:
            print(" ", end="")
    print()

print("12.")
n = 9

print("*" * n)

for i in range(3):
    print("*")

print("*" * n)

for i in range(3):
    print(" " * (n - 1) + "*")

print("*" * n)
