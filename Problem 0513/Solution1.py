# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        queue = [root]
        leftMost = root.val
        while len(queue):
            nextQueue = []
            while len(queue):
                curr = queue.pop(0)
                if curr.left:
                    nextQueue.append(curr.left)
                if curr.right:
                    nextQueue.append(curr.right)
            queue = nextQueue
            leftMost = nextQueue[0].val if len(nextQueue) else leftMost
        return leftMost
