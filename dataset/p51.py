from resounds import completions

def solveNQueens(n: int) -> list[list[str]]:
    """按照国际象棋的规则，皇后可以攻击与之处在同一行或同一列或同一斜线上的棋子。n皇后问题研究的是如何将n个皇后放置在n×n的棋盘上，并且使皇后彼此之间不能相互攻击。给你一个整数n，返回所有不同的n皇后问题的解决方案。每一种解法包含一个不同的n皇后问题的棋子放置方案，该方案中 'Q' 和 '.' 分别代表了皇后和空位。"""

code = completions(solveNQueens)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(solveNQueens(4))
