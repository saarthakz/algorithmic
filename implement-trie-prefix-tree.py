class TrieNode:
    def __init__(self):
        self.children = {}
        self.end = False
        pass


class PrefixTree:

    def __init__(self):
        self.root = TrieNode()
        self.st = set()

    def insert(self, word: str) -> None:
        if self.search(word):
            return

        self.st.add(word)
        root = self.root
        for char in word:
            if char not in root.children:
                root.children[char] = TrieNode()
            root = root.children.get(char)
        root.end = True

    def search(self, word: str) -> bool:
        return word in self.st

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for char in prefix:
            if char not in root.children:
                return False
            root = root.children.get(char)
        return True
