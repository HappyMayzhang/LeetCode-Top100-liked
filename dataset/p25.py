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

def reverseKGroup(head: Optional[ListNode], k: int) -> Optional[ListNode]:
    """给你链表的头节点 head ，每 k 个节点一组进行翻转，请你返回修改后的链表。"""

code = completions(reverseKGroup)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    head = list2node([1,2,3,4,5])
    print(node2list(reverseKGroup(head, 3)))
