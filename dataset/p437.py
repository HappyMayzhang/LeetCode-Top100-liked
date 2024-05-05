from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def pathSum(root: Optional[TreeNode], targetSum: int) -> int:
    """给定一个二叉树的根节点 root ，和一个整数 targetSum ，求该二叉树里节点值之和等于 targetSum 的路径的数目。路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。"""

code = completions(pathSum)
code = code.replace('self.', '')
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(10,
        left = TreeNode(5,
            left = TreeNode(3,
                left = TreeNode(3),
                right = TreeNode(-2)
            ),
            right = TreeNode(2,
                right = TreeNode(1)
            )
        ),
        right = TreeNode(-3,
            right = TreeNode(11)
        )
    )
    print(pathSum(root, 8))
