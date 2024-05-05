from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def isValidBST(root: Optional[TreeNode]) -> bool:
    """给你一个二叉树的根节点 root ，判断其是否是一个有效的二叉搜索树。
    有效二叉搜索树定义如下：
    节点的左子树只包含小于当前节点的数。
    节点的右子树只包含大于当前节点的数。
    所有左子树和右子树自身必须也是二叉搜索树。"""

code = completions(isValidBST)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(2,
        left = TreeNode(1),
        right = TreeNode(3)
    )
    print(isValidBST(root))
