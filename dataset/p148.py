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

def sortList(head: Optional[ListNode]) -> Optional[ListNode]:
    """给你链表的头结点 head ，请将其按升序排序。"""

code = completions(sortList)
code = code.replace('self.', '')
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    head = list2node([4,2,1,3])
    print(node2list(sortList(head)))
