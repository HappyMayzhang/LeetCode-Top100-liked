from resounds import completions

class TreeNode:
    def __init__(self, val, left = None, right = None):
        self.val = val
        self.left = left
        self.right = right

def lowestCommonAncestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    """给定一个二叉树, 找到该树中两个指定节点的最近公共祖先。
    百度百科中最近公共祖先的定义为：“对于有根树T的两个节点p、q，最近公共祖先表示为一个节点 x，满足x是p、q的祖先且x的深度尽可能大（一个节点也可以是它自己的祖先）。"""

code = completions(lowestCommonAncestor)
code = code.replace('self.', '')
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    p = TreeNode(5,
        left = TreeNode(6,
            left = TreeNode(0),
            right = TreeNode(8)
        ),
        right = TreeNode(2)
    )
    q = TreeNode(1,
        left = TreeNode(7),
        right = TreeNode(4)
    )
    root = TreeNode(3,
        left = p,
        right = q
    )
    print(lowestCommonAncestor(root, p, q))
