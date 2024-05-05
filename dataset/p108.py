from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def sortedArrayToBST(nums: list[int]) -> Optional[TreeNode]:
    """给你一个整数数组 nums ，其中元素已经按升序排列，请你将其转换为一棵平衡二叉搜索树。"""

code = completions(sortedArrayToBST)
code = code.replace('self.', '')
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = sortedArrayToBST([-10,-3,0,5,9])
    print([
        root.val,
        root.left.val, root.right.val,
        root.left.left.val, root.left.right,
        root.right.left.val
    ])
