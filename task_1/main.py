def solution(n: int, nums: []):
    for i in range(len(nums)):
        if nums[i] % 5 == 0:
            nums[i] = nums[i] // 5 * 2
        elif nums[i] % 2 == 0:
            nums[i] = nums[i] // 2 * 5
        print(nums[i], end = ' ')

if __name__ == '__main__':
    solution(3, [10, 2, 6, 20, 4, 5])


