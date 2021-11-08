def solution(a_cell: int, b_cell: int):
    res = 0
    #right
    if b_cell+2 < 9:
        if a_cell + 1 < 9:
            res += 1
        if a_cell-1 > 0:
            res += 1

    #left
    if b_cell-2 < 9 and b_cell-2 > 0:
        if a_cell + 1 < 9:
            res += 1
        if a_cell-1 > 0:
            res += 1

    #top
    if a_cell+2 < 9:
        if b_cell+1 < 9:
            res += 1
        if b_cell - 1 > 0:
            res += 1

    #bottom
    if a_cell-2 < 9 and a_cell-2 > 0:
        if b_cell+1 < 9:
            res += 1
        if b_cell-1 > 0:
            res += 1

    print(res)
if __name__ == '__main__':
    solution(8, 1)