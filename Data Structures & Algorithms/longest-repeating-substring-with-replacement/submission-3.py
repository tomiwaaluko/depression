class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        count = {}
        maxf = 0
        res = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)
            maxf = max(maxf, count[s[r]])

            while (r - l + 1) - maxf > k:
                count[s[l]] -= 1 # adjusting the counts
                l += 1 # shrinking the window from the left
            res = max(res, r - l + 1)
        return res
