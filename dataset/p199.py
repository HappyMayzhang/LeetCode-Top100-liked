from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root: Optional[TreeNode]) -> list[int]:
    """给定一个二叉树的根节点 root，想象自己站在它的右侧，按照从顶部到底部的顺序，返回从右侧所能看到的节点值。"""

code = completions(rightSideView)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(1,
        left = TreeNode(2,
            right = TreeNode(5)
        ),
        right = TreeNode(3,
            right = TreeNode(4)
        )
    )
    print(rightSideView(root))
