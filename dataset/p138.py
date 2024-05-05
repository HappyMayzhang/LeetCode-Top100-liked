from resounds import completions
from typing import Optional

class Node:
    def __init__(self, _val, _next = None, _random = None):
        self.val = _val
        self.next = _next
        self.random = _random

def list2node(a: list) -> Optional[Node]:
    return Node(a[0][0], list2node(a[1:])) if a else None

def node2list(n: Optional[Node]) -> list:
    return [[n.val, n.random], *node2list(n.next)] if n else []

def copyRandomList(head: Optional[Node]) -> Optional[Node]:
    """给你一个链表，每个节点包含一个额外增加的随机指针 random ，该指针可以指向链表中的任何节点或空节点。构造这个链表的深拷贝。"""

code = completions(copyRandomList)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    a = [[7,None],[13,0],[11,4],[10,2],[1,0]]
    head = list2node(a)
    head.next.random = head
    head.next.next.random = head.next.next.next.next
    head.next.next.next.random = head.next.next
    head.next.next.next.next.random = head
    print(node2list(copyRandomList(head)))
