class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        mp = defaultdict(int)

        for i, n in enumerate(numbers):
            tmp = target - n
            if mp[tmp]:
                return[mp[tmp], i + 1]
            mp[n] = i + 1
        return []
        