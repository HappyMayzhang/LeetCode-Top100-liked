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

def getIntersectionNode(headA: ListNode, headB: ListNode) -> Optional[ListNode]:
    """给你两个单链表的头节点 headA 和 headB ，请你找出并返回两个单链表相交的起始节点。"""

code = completions(getIntersectionNode)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    headA = list2node([4,1,8,4,5])
    headB = list2node([5,6,1,8,4,5])
    print(node2list(getIntersectionNode(headA, headB)))
