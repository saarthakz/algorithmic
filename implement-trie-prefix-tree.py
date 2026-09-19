"""
A prefix tree (also known as a trie) is a tree data structure used to efficiently store and retrieve keys in a set of strings. Some applications of this data structure include auto-complete and spell checker systems.

Implement the PrefixTree class:

    PrefixTree() Initializes the prefix tree object.
    void insert(String word) Inserts the string word into the prefix tree.
    boolean search(String word) Returns true if the string word is in the prefix tree (i.e., was inserted before), and false otherwise.
    boolean startsWith(String prefix) Returns true if there is a previously inserted string word that has the prefix prefix, and false otherwise.

"""


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
