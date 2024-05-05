from resounds import completions
import collections

def topKFrequent(nums: list[int], k: int) -> list[int]:
    """给你一个整数数组nums和一个整数k，请你返回其中出现频率前k高的元素。你可以按任意顺序返回答案。"""

code = completions(topKFrequent)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(topKFrequent([1,1,1,2,2,3], 2))
