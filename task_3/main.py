stolb_1 = int(input("stolb 1: "))
element_1 = int(input("element 1: "))
stolb_2 = int(input("stolb 2: "))
element_2 = int(input("element 2: "))

elements_list = []

for i in range(1, 64+1):
    elements_list.append(i)

res = []

def what_is_element(stolb: int, element: int):
    if stolb % 2 == 0:
        if stolb > 1:
            element_number = ((stolb-1) * 8) + (8 - element)
            res.append(element_number)
        else:
            element_number = element
            res.append(element_number)
    else:
        element_number = ((stolb - 1) * 8) + (8 - (8 - (element + 1)))
        res.append(element_number)


what_is_element(stolb_1, element_1)
what_is_element(stolb_2, element_2)

for i in range(2):
    if res[i] % 2 == 0:
        res[i] = 1
    else:
        res[i] = 2


if res[0] == res[1]:
    print("yes")
else:
    print("no")

#або можна додуматись до такого, що якщо додати всі часла на вході, і перевірити на кратність,
#то програма теж спрацює
#summ = 0
#for i in range(4):
#    summ += int(input())
#if summ % 2 == 0:
#    print("yes")
#else:
#    print("no")