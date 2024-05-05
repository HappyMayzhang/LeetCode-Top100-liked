from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root: Optional[TreeNode]) -> bool:
    """给你一个二叉树的根节点 root ， 检查它是否轴对称。"""

code = completions(isSymmetric)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(1,
        left = TreeNode(2,
            left = TreeNode(3),
            right = TreeNode(4)
        ),
        right = TreeNode(2,
            left = TreeNode(4),
            right = TreeNode(3)
        )
    )
    print(isSymmetric(root))
