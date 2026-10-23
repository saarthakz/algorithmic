"""
You are given two words, beginWord and endWord, and also a list of words wordList. All of the given words are of the same length, consisting of lowercase English letters, and are all distinct.

Your goal is to transform beginWord into endWord by following the rules:

    You may transform beginWord to any word within wordList, provided that at exactly one position the words have a different character, and the rest of the positions have the same characters.
    You may repeat the previous step with the new word that you obtain, and you may do this as many times as needed.

Return the minimum number of words within the transformation sequence needed to obtain the endWord, or 0 if no such sequence exists.
"""

from typing import List, Dict, Set, Deque
from collections import deque


class Solution:
    def ladderLength(self, begin_word: str, end_word: str, word_list: List[str]) -> int:

        word_set = set(word_list)

        if end_word not in word_set:
            return 0

        word_set.add(begin_word)

        wildcard_mapping: Dict[str, Set[str]] = {}

        for word in word_set:
            char_arr = list(word)
            for idx in range(len(char_arr)):
                original_char = char_arr[idx]
                char_arr[idx] = "*"
                wildcard = "".join(char_arr)
                wildcard_mapping.setdefault(wildcard, set()).add(word)
                char_arr[idx] = original_char

        adj_list = {}

        for word in word_set:
            edges: Set[str] = set()
            char_arr = list(word)
            for idx in range(len(char_arr)):
                original_char = char_arr[idx]
                char_arr[idx] = "*"
                edge = "".join(char_arr)
                edges.add(edge)
                char_arr[idx] = original_char

            neighbours: Set[str] = set()

            for edge in edges:
                neighbours.update(wildcard_mapping.get(edge, set()))
                neighbours.discard(word)

            adj_list[word] = neighbours

        INT_MAX = int(1e10)
        min_dis = INT_MAX
        visited: Set[str] = set()

        queue = deque([(begin_word, 1)])

        while len(queue):
            curr, curr_dis = queue.popleft()

            if curr == end_word:
                return curr_dis

            if curr in visited:
                continue

            visited.add(curr)

            for neighbour in adj_list[curr]:
                queue.append((neighbour, curr_dis + 1))

        return 0
