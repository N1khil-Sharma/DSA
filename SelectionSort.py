def nigga(nums):
    n = len(nums)-1
    for i in range(n):
        mini = i
        for j in range(i+1, n+1):
            if nums[j] < nums[mini]:
                mini = j
        nums[i], nums[mini] = nums[mini], nums[i]
    return nums
x = eval(input("Enter unsorted array"))
print(nigga(x))