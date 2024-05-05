from resounds import completions

def uniquePaths(m: int, n: int) -> int:
    """一个机器人位于一个mxn网格的左上角（起始点在下图中标记为 “Start” ）。机器人每次只能向下或者向右移动一步。机器人试图达到网格的右下角（在下图中标记为 “Finish” ）。问总共有多少条不同的路径？"""

code = completions(uniquePaths)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(uniquePaths(3, 7))
