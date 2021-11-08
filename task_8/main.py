import operator
def solution(students_count: int, students_list = {}):
    for i in range(len(students_list)):
        if students_count > 10000 or students_count < 1:
            print("enter the correct numbers!")
            exit()
        elif list(students_list)[i] > 100000 or list(students_list.values())[i] > 100000:
            print("enter the correct numbers!")
            exit()

    #сортуєм словарь по зростанню
    sorted_values = sorted(students_list.items(), key=operator.itemgetter(1))

    #витягуєм по 2 останні значення з кожного списка
    for i in range(1, len(sorted_values)+1):
        print(sorted_values[len(sorted_values) - i][0], sorted_values[len(sorted_values) - i][1])

if __name__ == '__main__':
    solution(3, {101:80, 305:90, 200:14})

