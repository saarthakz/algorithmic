"""
Design a data structure that supports adding new words and searching for existing words.

Implement the WordDictionary class:

    void addWord(word) Adds word to the data structure.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise. word may contain dots '.' where dots can be matched with any letter.

"""


class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
        self.end = False
        pass


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()
        self.st = set()

    def addWord(self, word: str) -> None:
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
        if not self._search_key_has_wildcard(word):
            return word in self.st
        else:
            return self._search_helper(word, self.root)

    def _search_helper(self, word: str, dic_root: TrieNode) -> bool:
        root = dic_root
        for idx, char in enumerate(word):

            # If not wild card character (Normal search process)
            if char != ".":
                if char not in root.children:
                    return False
                root = root.children.get(char)

            # Found the wildcard
            else:
                for key in root.children.keys():
                    if self._search_helper(word[idx + 1 :], root.children.get(key)):
                        return True
                return False
        return root.end

    def _search_key_has_wildcard(self, word: str) -> bool:
        for char in word:
            if char == ".":
                return True
        return False
