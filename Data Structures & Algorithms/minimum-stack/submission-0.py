class MinStack:

    def __init__(self):
        #defining two stacks, actual and getmin 
        self.stack = []
        self.minStack = []

    def push(self, val: int) -> None:
        #always taking the input val and appending it to the first stack
        self.stack.append(val)
        val = min(val, self.minStack[-1] if self.minStack else val)
        self.minStack.append(val)
        

    def pop(self) -> None:
        #popping from both of the stacks
        self.stack.pop()
        self.minStack.pop()

    def top(self) -> int:
        # getting the top val by taking the top of the first stack
        return self.stack[-1]

    def getMin(self) -> int:
        # getting the top val by taking the top of the second stack
        return self.minStack[-1]

        
