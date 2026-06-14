def bubbles(nums):
    n = len(nums)
    for i in range(n-1, -1, -1):
        for j in range(i):
            if nums[j] > nums[j+1]:
                nums[j] , nums[j+1] = nums[j+1] , nums[j]
    return nums

x = eval(input("Please enter an unsorted array: "))
print(bubbles(x))