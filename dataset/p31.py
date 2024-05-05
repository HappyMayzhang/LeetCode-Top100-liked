from resounds import completions

def nextPermutation(nums: list[int]) -> None:
    """如果数组的所有排列根据其字典顺序从小到大排列在一个容器中，那么数组的下一个排列就是在这个有序容器中排在它后面的那个排列。如果不存在下一个更大的排列，那么这个数组必须重排为字典序最小的排列（即，其元素按升序排列）。
    例如，arr = [1,2,3] 的下一个排列是 [1,3,2] 。
    类似地，arr = [2,3,1] 的下一个排列是 [3,1,2] 。
    而 arr = [3,2,1] 的下一个排列是 [1,2,3] ，因为 [3,2,1] 不存在一个字典序更大的排列。"""

code = completions(nextPermutation)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    nums = [1,2,3]
    nextPermutation(nums)
    print(nums)
