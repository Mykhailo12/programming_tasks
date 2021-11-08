def solution(file_dir: str):
    words = []
    #розбиття файлу на слова, додання в список
    with open(file_dir, 'r') as f:
        for i in f:
            for j in i.split():
               words.append(j)

    res_list = []

    #виділяєм кожен другий елемент в інший список))))))))
    for i in range(len(words)):
        if i % 2 == 0:
            res_list.append(words[i])

    count = 1

    #перевіряєм вихіжний список на належність одинакових елементів
    for i in range(len(res_list)-1):
        for j in range(i+1, len(res_list)):
            if res_list[i] == res_list[j]:
                count+=1
                #вивод
                print(res_list[i], count)

if __name__ == '__main__':
    solution('input.txt')


