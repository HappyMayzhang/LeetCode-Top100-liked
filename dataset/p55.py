from resounds import completions

def canJump(nums: list[int]) -> bool:
    """给你一个非负整数数组nums，你最初位于数组的第一个下标。数组中的每个元素代表你在该位置可以跳跃的最大长度。判断你是否能够到达最后一个下标，如果可以，返回 true ；否则，返回 false 。"""

code = completions(canJump)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(canJump([2,3,1,1,4]))
