from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    """返回一棵二叉树的直径。二叉树的直径是指树中任意两个节点之间最长路径的长度。两节点之间路径的长度由它们之间边数表示。"""

code = completions(diameterOfBinaryTree)
code = code.replace('self.', '')
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(1,
        left = TreeNode(2,
            left = TreeNode(4),
            right = TreeNode(5)
        ),
        right = TreeNode(3)
    )
    print(diameterOfBinaryTree(root))
