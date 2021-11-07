a = []
b = []

k = int(input("к-сть чоловік "))
w = int(input("максимальна вага палаток "))

for i in range(1, 4):
    b.append(int(input(f'b{i}: ')))
    a.append(int(input(f'a{i}: ')))

tents_mass = 0
tents_capacity = 0

def error():
    print("error, enter the correct numbers")
    exit()

for j in range(3):
    if b[j] > 15 or k > 15:
        error()
    elif b[j] < 1 or a[j] < 1 or w < 1 or k < 1:
        error()
    elif w > 30:
        error()
    elif a[j] > 10:
        error()

    tents_mass += a[j]
    tents_capacity += b[j]


if tents_capacity < k:
    print("NO")
elif tents_mass > w:
    print("NO")
else:
    print("YES")







