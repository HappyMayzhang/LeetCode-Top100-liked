from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root: Optional[TreeNode]) -> Optional[TreeNode]:
    """给你一棵二叉树的根节点 root ，翻转这棵二叉树，并返回其根节点。"""

code = completions(invertTree)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(4,
        left = TreeNode(2,
            left = TreeNode(1),
            right = TreeNode(3)
        ),
        right = TreeNode(7,
            left = TreeNode(6),
            right = TreeNode(9)
        )
    )
    toor = invertTree(root)
    print([
        toor.val,
        toor.left.val, toor.right.val,
        toor.left.left.val, toor.left.right.val,
        toor.right.left.val, toor.right.right.val
    ])
