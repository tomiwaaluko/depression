class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {")" : "(", "]" : "[", "}" : "{"}

        for i in s:
            if i in hmap:
                if stack and stack[-1] == hmap[i]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(i)
        return True if not stack else False