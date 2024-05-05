from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def kthSmallest(root: Optional[TreeNode], k: int) -> int:
    """给定一个二叉搜索树的根节点root，和一个整数k，请你设计一个算法查找其中第k个最小元素（从1开始计数）。"""

code = completions(kthSmallest)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(3,
        left = TreeNode(1,
            right = TreeNode(2)
        ),
        right = TreeNode(4)
    )
    print(kthSmallest(root, 1))
