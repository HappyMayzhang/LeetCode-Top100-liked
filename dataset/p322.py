from resounds import completions

def coinChange(coins: list[int], amount: int) -> int:
    """给你一个整数数组coins，表示不同面额的硬币；以及一个整数amount，表示总金额。计算并返回可以凑成总金额所需的最少的硬币个数。如果没有任何一种硬币组合能组成总金额，返回-1。你可以认为每种硬币的数量是无限的。"""

code = completions(coinChange)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(coinChange([1, 2, 5], 11))
