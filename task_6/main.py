def solution(k: int, w: int, a = [], b =[]):
    tents_mass = 0
    tents_capacity = 0

    #щоб 100 раз не писати
    def error():
        print("error, enter the correct numbers")
        exit()

    #перевірочки
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
        tents_capacity += a[j]

    if tents_capacity < k:
        print("NO")
    elif tents_mass > w:
        print("NO")
    else:
        print("YES")

if __name__ == '__main__':
    solution(12, 20, [3, 7, 6], [4, 6, 5])







