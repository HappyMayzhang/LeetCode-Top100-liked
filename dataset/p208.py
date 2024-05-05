from resounds import completions

class Trie:
    """前缀树 是一种树形数据结构，用于高效地存储和检索字符串数据集中的键。"""

    def __init__(self):
        """初始化前缀树对象。"""
        #self.node = set()
        ...

    def insert(self, word: str) -> None:
        """向前缀树中插入字符串 word 。"""
        #self.node.add(word)
        ...

    def search(self, word: str) -> bool:
        """如果字符串 word 在前缀树中，返回 true ；否则，返回 false 。"""
        #return word in self.node
        ...

    def startsWith(self, prefix: str) -> bool:
        """如果之前插入的字符串 word 的前缀之一为 prefix ，返回 true ；否则，返回 false 。"""
        #return any([word.startswith(prefix) for word in self.node])
        ...

code = completions(Trie)
print('-' * 8)
print(code)
print('-' * 8)
exec(code)

if __name__ == "__main__":
    trie = Trie()
    trie.insert("apple")
    print(trie.search("apple"))
    print(trie.search("app"))
    print(trie.startsWith("app"))
    trie.insert("app")
    print(trie.search("app"))
