class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h= {}
        for i, num in enumerate(nums):
            d = target - num
            if d in h:
                return ([h[d], i])
            h[num] = i
