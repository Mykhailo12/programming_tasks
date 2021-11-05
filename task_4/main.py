#задачу списав у мужика, розбирусь в коді, і мб нарию схожу, такі задачі досить цікаві.

vvod = int(input())
num = vvod ** 0.5
if int(num) != num:
    num = int(num)

table = [[0] * num for i in range(num)]
numb = 0
ivert = num
for i in range(num):
    if ivert > 0:
        igoriz = 0
        for i in range(num - ivert+1):
            if igoriz <= num - ivert:
                numb += 1
                if numb <= vvod:
                    table[igoriz][ivert + igoriz - 1] = numb
                else:
                    table[igoriz][ivert + igoriz - 1] = 0
            igoriz += 1
    ivert -= 1
ivert = 1
for i in range(num - 1):
    if ivert < num:
        igoriz = 0
        for i in range(num - ivert):
            if igoriz < num - ivert:
                numb += 1
                if numb <= vvod:
                    table[ivert + igoriz][igoriz] = numb
                else:
                    table[ivert + igoriz][igoriz] = 0
            igoriz += 1
    ivert += 1
for row in table:
    for elem in row:
        print(elem, end = ' ')
    print()