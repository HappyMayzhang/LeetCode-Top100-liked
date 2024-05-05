from resounds import completions

def dailyTemperatures(temperatures: list[int]) -> list[int]:
    """给定一个整数数组temperatures，表示每天的温度，返回一个数组answer，其中answer[i]是指对于第i天，下一个更高温度出现在几天后。如果气温在这之后都不会升高，请在该位置用0来代替。"""

code = completions(dailyTemperatures)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(dailyTemperatures([73,74,75,71,69,72,76,73]))
