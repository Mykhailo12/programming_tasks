def solution(stolb_1: int, element_1: int, stolb_2: int, element_2: int):
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

    if res[0] % 2 == 0 and res[1] % 2 == 0:
        print("Yes")
    elif res[0] % 2 != 0 and res[1] % 2 != 0:
        print("Yes")
    else:
        print("N")

if __name__ == '__main__':
    solution(1, 1, 2, 6)