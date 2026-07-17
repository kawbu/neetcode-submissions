# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root: return []
        res = []
        queue = deque()
        queue.append((root, 0))
        while queue:
            curr, idx = queue.popleft()
            if len(res) <= idx:
                res.append([])
            res[idx].append(curr.val)
            if curr.left:
                queue.append((curr.left, idx + 1))
            if curr.right:
                queue.append((curr.right, idx + 1))
        return res