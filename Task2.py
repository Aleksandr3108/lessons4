n = int(input("Введіть число n:"))
s = 0
for i in range(1, n, 2):
    print(i, end = ",")
    s = s + i
print()
print("Sum =", s)