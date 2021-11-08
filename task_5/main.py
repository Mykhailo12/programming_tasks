def solution(a: int, b: int, c: int):
    cubs = a * b * c
    #кутові (незафарбовані 3 сторони)
    angle_cubs = 0
    #реберні (незафарбовані 4 сторони)
    x_cubs = 0
    #реберні, знаходяться на частині з кутовими
    x_angle_cubs = 0
    #середенні (незафрбовані 5 сторін)
    y_cubs = 0
    #центрові (повністю чисті)
    full_clean_cubs = 0

    res = 0

    #провірки, для брусків з сторонами до 3дм
    if a and b < 3:
        #a = 1, b = 1
        if a + b <= 2:
            if c > 2:
                angle_cubs = 2
                x_cubs = 2 * (c - 2)
            else:
                angle_cubs = 2
        #a = 1, b = 2 і наоборот
        if a + b == 3:
            if c > 2:
                angle_cubs = 8
                x_cubs = 6 * (c-2)
            else:
                angle_cubs = 8
        #a = 2, b = 2
        if a + b == 4:
            if c > 2:
                angle_cubs = 24
                x_cubs = 16 * (c-2)
            else:
                angle_cubs = 24
        res = angle_cubs + x_cubs
    #провірки, для брусків з сторонами від 3дм
    elif b and a > 2:
        #якщо c > 2, то в рахунок додаються серединні блоки кубиків
        if c > 2:
            angle_cubs = 24
            x_cubs = 16 * (c - 2)
            x_angle_cubs = (((((a+b)-2)*2) - 4) * 4) * 2
            y_cubs =  (((a-2)*(b-2)) * 2 + ((((a+b)-2)*2)-4)*(c-2))*5
            full_clean_cubs = (((a-2)*(b-2)) * (c-2)) * 6
        #якщо c <= 2, то в рахуються тільки карйні блоки кубиків
        elif c <= 2:
            angle_cubs = 24
            x_angle_cubs = ((((a+b)-2)*2) - 4) * 4
            y_cubs = ((a-2)*(b-2)) * 2

        res = (angle_cubs + x_cubs + x_angle_cubs + y_cubs + full_clean_cubs)

    print(cubs, res)

if __name__ == '__main__':
    solution(1, 2, 3)