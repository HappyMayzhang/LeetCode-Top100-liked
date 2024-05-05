from resounds import completions

def groupAnagrams(strs: list[str]) -> list[list[str]]:
    """给你一个字符串数组，请你将字母异位词组合在一起。可以按任意顺序返回结果列表。字母异位词是由重新排列源单词的所有字母得到的一个新单词。"""

code = completions(groupAnagrams)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    print(groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
