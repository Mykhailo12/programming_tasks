def solution(file_dir: str):
    file = open(file_dir)

    pers_dict = []

    #додавання данних в список
    for pers in file:
        #розбивання файлу на слова
        data = pers.split()

        #додавання ім'я і рівня персонажів в елемент списку
        pers_dict.append((data[1], int(data[0])))

    #сортуєм від найбільшого до найменшого
    pers_dict.sort(key=lambda elem: elem[1], reverse = True)

    command1 = []
    command2 = []
    summa1 = 0
    summa2 = 0

    #заповнення списків двох команд
    for elem in pers_dict:
        if summa1 <= summa2:
            command1.append(elem)
            summa1 += elem[1]
        else:
            command2.append(elem)
            summa2 += elem[1]

    print(summa1, summa2)
    print(command1)
    print(command2)
    #вивод 1 команди
    for key in command1:
        print(key[0])
    #вивод різниці рівнів обох команд
    if summa1 > summa2:
        print(summa1-summa2)
    else:
        print(summa2-summa1)
    #вивод 2 команди
    for key in command2:
        print(key[0])


if __name__ == '__main__':
    solution('input.txt')