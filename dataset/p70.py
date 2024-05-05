from resounds import completions

def climbStairs(n: int) -> int:
    """假设你正在爬楼梯。需要n阶你才能到达楼顶。每次你可以爬1或2个台阶。你有多少种不同的方法可以爬到楼顶呢？"""

code = completions(climbStairs)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(climbStairs(2))
