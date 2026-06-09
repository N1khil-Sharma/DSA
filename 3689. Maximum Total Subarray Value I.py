class Solution:
    def maxTotalValue(self, nums: List[int], k: int) -> int:
        max = 0
        min = inf
        for i in nums:
            if i>max:
                max = i
            if i<min:
                min = i
        return (max-min) * k
