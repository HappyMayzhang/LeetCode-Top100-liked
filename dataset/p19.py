from resounds import completions
from typing import Optional

class ListNode:
    def __init__(self, _val, _next = None):
        self.val = _val
        self.next = _next
    def __eq__(self, other):
        return self.val == other.val if other else False

def list2node(a: list) -> Optional[ListNode]:
    return ListNode(a[0], list2node(a[1:])) if a else None

def node2list(n: Optional[ListNode]) -> list:
    return [n.val, *node2list(n.next)] if n else []

def removeNthFromEnd(head: Optional[ListNode], n: int) -> Optional[ListNode]:
    """给你一个链表，删除链表的倒数第 n 个结点，并且返回链表的头结点。"""

code = completions(removeNthFromEnd)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    head = list2node([1,2,3,4,5])
    print(node2list(removeNthFromEnd(head, 2)))
