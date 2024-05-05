from resounds import completions

def maxSlidingWindow(nums: list[int], k: int) -> list[int]:
    """给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位。返回滑动窗口中的最大值 。"""

code = completions(maxSlidingWindow)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))
