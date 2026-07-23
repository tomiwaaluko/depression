class Solution:
    def isValid(self, s: str) -> bool:
        #creating a stack
        stack = [] 
        # creating a hashmap for all three types of characters
        hmap = {")" : "(", "]" : "[", "}" : "{"}

        # going through every character in the input string
        for c in s:
            #checking if the character is a closing parenthesis
            if c in hmap:
                # making sure the stack isn't empty & if the value at the top of the
                # stack is the matching open parenthesis
                if stack and stack[-1] == hmap[c]:
                    stack.pop()
                # if they dont match each other or the stack is empty
                else:
                    return False
            # if we get an open parenthesis...
            else:
                stack.append(c)
        # ONLY return true if the STACK IS EMPTY
        return True if not stack else False