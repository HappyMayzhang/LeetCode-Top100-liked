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

def addTwoNumbers(l1: ListNode, l2: ListNode) -> ListNode:
    """给你两个非空的链表，表示两个非负的整数。它们每位数字都是按照逆序的方式存储的，并且每个节点只能存储一位数字。请你将两个数相加，并以相同形式返回一个表示和的链表。"""

code = completions(addTwoNumbers)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    l1 = list2node([2,4,3])
    l2 = list2node([5,6,4])
    print(node2list(addTwoNumbers(l1, l2)))
