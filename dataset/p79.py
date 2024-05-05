from resounds import completions

def exist(board: list[list[str]], word: str) -> bool:
    """给定一个mxn二维字符网格board和一个字符串单词word。如果word存在于网格中，返回True；否则，返回False。单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。"""

code = completions(exist)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"))
