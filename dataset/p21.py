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

def mergeTwoLists(list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
    """将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。"""

code = completions(mergeTwoLists)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    list1 = list2node([1,2,4])
    list2 = list2node([1,3,4])
    print(node2list(mergeTwoLists(list1, list2)))
