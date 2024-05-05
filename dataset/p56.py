from resounds import completions

def merge(intervals: list[list[int]]) -> list[list[int]]:
    """以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返回一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。"""

code = completions(merge)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(merge([[1,3],[2,6],[8,10],[15,18]]))
