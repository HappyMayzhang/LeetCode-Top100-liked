from resounds import completions

def combinationSum(candidates: list[int], target: int) -> list[list[int]]:
    """给你一个 无重复元素 的整数数组candidates和一个目标整数target，找出candidates中可以使数字和为目标数target的所有不同组合 ，并以列表形式返回。你可以按任意顺序返回这些组合。candidates 中的同一个数字可以无限制重复被选取 。如果至少一个数字的被选数量不同，则两种组合是不同的。 对于给定的输入，保证和为 target 的不同组合数少于 150 个。"""

code = completions(combinationSum)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(combinationSum([2,3,6,7], 7))
