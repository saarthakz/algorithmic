from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.rows = len(board)
        self.cols = len(board[0])
        self.board = board

        # Go from top-left -> bottom-right of the board
        for row in range(self.rows):
            for col in range(self.cols):

                # Potential search starting point
                if board[row][col] == word[0]:
                    if self.helper(word, (row, col), set()):
                        return True

        return False

    def helper(self, word: str, board_indices: tuple[int, int], visited: set):

        # Base case for true
        if len(word) == 0:
            return True

        if board_indices in visited:
            return False

        row, col = board_indices

        # Base case for false (Out of bounds)
        if row < 0 or row >= self.rows or col < 0 or col >= self.cols:
            return False

        # If current character is not matching the current character for the given word, we are done searching this path
        if self.board[row][col] != word[0]:
            return False

        visited.add(board_indices)

        return (
            self.helper(word[1:], (row + 1, col), set(visited))
            or self.helper(word[1:], (row - 1, col), set(visited))
            or self.helper(word[1:], (row, col + 1), set(visited))
            or self.helper(word[1:], (row, col - 1), set(visited))
        )
