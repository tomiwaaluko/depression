# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []

        q = collections.deque() # creates empty queue
        q.append(root) # adding theroot node into the queue

        while q:
            qLen = len(q) # counts how many nodes are in the level (ex. qLen = 4 if at level 3)
            level = [] # creates an empty list to store values from the current row

            for i in range(qLen): # process every node in the level
                node = q.popleft() # remove the next node from the queue
                if node: #checks if node exsists
                    level.append(node.val) #adds the node value to the level list
                    q.append(node.left) #adds the left and right child to the queue
                    q.append(node.right)
            if level: #checks if `level` is not empty
                    res.append(level) # example: [[1],[2,3],[4,5,6,7]]
        return res