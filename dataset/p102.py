from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def levelOrder(root: Optional[TreeNode]) -> list[list[int]]:
    """广度遍历二叉树。"""

code = completions(levelOrder)
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
    print(levelOrder(root))
