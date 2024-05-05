from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root: Optional[TreeNode]) -> list[int]:
    """给定一个二叉树的根节点 root ，返回它的中序遍历。"""

code = completions(inorderTraversal)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(1,
        right = TreeNode(2,
            left = TreeNode(3)
        )
    )
    print(inorderTraversal(root))
