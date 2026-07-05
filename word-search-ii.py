class TrieNode:
    def __init__(self):
        self.children: dict[str, TrieNode] = {}
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


from typing import List


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        self.board = board
        self.tree = PrefixTree()
        self.ans_list = set()

        for word in words:
            self.tree.insert(word)

        self.row = len(board)
        self.col = len(board[0])

        for row in range(self.row):
            for col in range(self.col):
                if board[row][col] in self.tree.root.children:
                    # Navigate the board
                    self.helper(
                        row,
                        col,
                        board[row][col],
                        set(),
                        self.tree.root.children.get(board[row][col]),
                    )

        return list(self.ans_list)

    def helper(
        self, row: int, col: int, trail: str, visited: set, dict_node: TrieNode
    ) -> None:
        # If the current node is marked as end, then the current trail is a word, found in the board
        if dict_node.end:
            self.ans_list.add(trail)

        # Mark the current (row, col) as visited
        visited.add((row, col))

        # For each of the possible neighbours check:
        # 1. If they are in bounds.
        # 2. If they are in the current node's children.

        possible_neighbours = [
            (row + 1, col),
            (row - 1, col),
            (row, col + 1),
            (row, col - 1),
        ]

        for next_row, next_col in possible_neighbours:
            if (
                not self._in_bound(next_row, next_col)
                or (next_row, next_col) in visited
            ):
                continue
            next_char = self.board[next_row][next_col]

            if next_char in dict_node.children:
                self.helper(
                    next_row,
                    next_col,
                    trail + next_char,
                    set(visited),
                    dict_node.children.get(next_char),
                )

    def _in_bound(self, row: int, col: int):
        return row >= 0 and row < self.row and col >= 0 and col < self.col

