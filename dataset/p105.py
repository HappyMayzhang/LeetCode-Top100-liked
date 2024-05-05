from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def buildTree(preorder: list[int], inorder: list[int]) -> Optional[TreeNode]:
    """给定两个整数数组preorder和inorder，其中preorder是二叉树的先序遍历，inorder是同一棵树的中序遍历，用这两个数组构造二叉树。"""

code = completions(buildTree)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = buildTree([3,9,20,15,7], [9,3,15,20,7])
    print([
        root.val,
        root.left.val, root.right.val,
        root.left.left, root.left.right,
        root.right.left.val, root.right.right.val
    ])
