a = int(input("a: "))
b = int(input("b: "))

res = 0
#right
if b + 2 < 9:
    if a + 1 < 9:
        res += 1

    if a - 1 > 0:
        res += 1

#left
if b - 2 < 9 and b - 2 > 0:
    if a + 1 < 9:
        res += 1

    if a - 1 > 0:
        res += 1

#top
if a + 2 < 9:
    if b + 1 < 9:
        res += 1

    if b - 1 > 0:
        res += 1

#bottom
if a - 2 < 9 and a - 2 > 0:
    if b + 1 < 9:
        res += 1

    if b - 1 > 0:
        res += 1

print(res)