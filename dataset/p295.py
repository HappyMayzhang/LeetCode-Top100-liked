from resounds import completions

class MedianFinder:
    """中位数是有序整数列表中的中间值。如果列表的大小是偶数，则没有中间值，中位数是两个中间值的平均值。"""

    def __init__(self):
        """初始化 MedianFinder 对象。"""
        ...

    def addNum(self, num: int) -> None:
        """将数据流中的整数 num 添加到数据结构中。"""
        ...

    def findMedian(self) -> float:
        """返回到目前为止所有元素的中位数。"""
        ...

code = completions(MedianFinder)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    medianFinder = MedianFinder()
    medianFinder.addNum(1)
    medianFinder.addNum(2)
    print(medianFinder.findMedian())
    medianFinder.addNum(3)
    print(medianFinder.findMedian())
