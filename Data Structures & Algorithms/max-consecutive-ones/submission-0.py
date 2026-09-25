class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0
        for i in nums:
            count = count + 1 if i else 0
            res = max(res, count)
        return res