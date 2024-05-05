from resounds import completions
from typing import Optional

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def flatten(root: Optional[TreeNode]) -> None:
    """给你二叉树的根结点 root ，请你将它展开为一个单链表：
    展开后的单链表应该同样使用 TreeNode ，其中 right 子指针指向链表中下一个结点，而左子指针始终为 None 。展开后的单链表应该与二叉树先序遍历顺序相同。"""

code = completions(flatten)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    root = TreeNode(1,
        left = TreeNode(2,
            left = TreeNode(3),
            right = TreeNode(4)
        ),
        right = TreeNode(5,
            right = TreeNode(6)
        )
    )
    flatten(root)
    print([
        root.val, root.left,
        root.right.val, root.right.left,
        root.right.right.val, root.right.right.left,
        root.right.right.right.val, root.right.right.right.left,
        root.right.right.right.right.val, root.right.right.right.right.left,
        root.right.right.right.right.right.val
    ])
