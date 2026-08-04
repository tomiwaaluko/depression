class MinStack:

    def __init__(self):
        #initialize main and min stack
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        #append the input value to the main stack first
        self.stack.append(val) 
        val = min(val, self.minStack[-1] if self.minStack else val) #computing the new minimum
        self.minStack.append(val)
        

    def pop(self) -> None:
        #popping from both stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # returning the top of the main stack
        return self.stack[-1]

    def getMin(self) -> int:
        # returning the top of the min stack
        return self.minStack[-1]
