from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root: Optional[TreeNode]) -> int:
    """给定一个二叉树 root ，返回其最大深度。二叉树的最大深度是指从根节点到最远叶子节点的最长路径上的节点数。"""

code = completions(maxDepth)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(3,
        left = TreeNode(9),
        right = TreeNode(20,
            left = TreeNode(15),
            right = TreeNode(7)
        )
    )
    print(maxDepth(root))
