from resounds import completions

def orangesRotting(grid: list[list[int]]) -> int:
    """在给定的mxn网格 grid 中，每个单元格可以有以下三个值之一：
    值0代表空单元格；
    值1代表新鲜橘子；
    值2代表腐烂的橘子。
    每分钟腐烂的橘子周围4个方向上相邻的新鲜橘子都会腐烂。计算全烂了需要多长时间？"""

code = completions(orangesRotting)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(orangesRotting([
        [2,1,1],
        [1,1,0],
        [0,1,1]
    ]))
