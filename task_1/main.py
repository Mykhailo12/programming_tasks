nums = int(input())
listnums = []
for i in range(nums):
    listnums.append(int(input()))
for i in range(nums):
    if listnums[i] % 5 == 0:
        listnums[i] = listnums[i] // 5 * 2
    elif listnums[i] % 2 == 0:
        listnums[i] = listnums[i] // 5 * 2
    print(listnums[i], end = ' ')

