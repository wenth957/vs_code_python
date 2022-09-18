class Trie:

    def __init__(self):
        self.son = [[None for _ in range(26)] for _ in range(100010)]
        self.idx = 1
        self.cnt = [None for i in range(100010)]
    def insert(self, word: str) -> None:
        root = 0
        for i in range(len(word)):
            u = ord(word[i]) - ord('a')
            if self.son[root][u] is None:
                self.son[root][u] = self.idx
                self.cnt[self.idx] = 0
                self.idx += 1
            root = self.son[root][u]
        self.cnt[root] += 1

    def query(self, prefix: str):
        root = 0
        for i in range(len(prefix)):
            u = ord(prefix[i]) - ord('a')
            if self.son[root][u] is None:
                return None
            root = self.son[root][u]
        return root

    def search(self, word: str) -> bool:
        node = self.query(word)
        return False if node is None else self.cnt[node] > 0

    def startsWith(self, prefix: str) -> bool:
        node = self.query(prefix)
        return False if node is None else True
