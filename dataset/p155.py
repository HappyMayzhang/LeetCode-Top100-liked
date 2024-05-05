from resounds import completions

class MinStack:
    """一个支持 push ，pop ，top 操作，并能在常数时间内检索到最小元素的栈。"""

    def __init__(self):
        """初始化堆栈对象。"""
        ...

    def push(self, val: int) -> None:
        """将元素val推入堆栈。"""
        ...

    def pop(self) -> None:
        """删除堆栈顶部的元素。"""
        ...

    def top(self) -> int:
        """获取堆栈顶部的元素。"""
        ...

    def getMin(self) -> int:
        """获取堆栈中的最小元素。"""
        ...

code = completions(MinStack)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    minStack = MinStack()
    minStack.push(-2)
    minStack.push(0)
    minStack.push(-3)
    print(minStack.getMin())
    minStack.pop()
    print(minStack.top())
    print(minStack.getMin())
