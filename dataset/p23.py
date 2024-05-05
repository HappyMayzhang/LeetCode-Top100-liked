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

def mergeKLists(lists: list[Optional[ListNode]]) -> Optional[ListNode]:
    """给你一个链表数组，数组中每个链表都已经按升序排列。请你将所有链表合并到一个升序链表中。不要使用类。"""

code = completions(mergeKLists)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    lists = [
        list2node([1,4,5]),
        list2node([1,3,4]),
        list2node([2,6])
    ]
    print(node2list(mergeKLists(lists)))
