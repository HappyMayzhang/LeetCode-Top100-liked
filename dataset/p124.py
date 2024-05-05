from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def maxPathSum(root: Optional[TreeNode]) -> int:
    """路径和是路径中各节点值的总和，计算最大路径和。二叉树中的路径被定义为一条节点序列，序列中每对相邻节点之间都存在一条边。同一个节点在一条路径序列中至多出现一次。"""

code = completions(maxPathSum)
code = code.replace('self.', '_')
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(1,
        left = TreeNode(2),
        right = TreeNode(3)
    )
    print(maxPathSum(root))
