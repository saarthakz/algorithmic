"""
Given two strings s and t, return true if the two strings are anagrams of each other, otherwise return false.

Two strings are anagrams if they contain the same characters, with each character appearing the same number of times, regardless of order.
"""


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # Anagrams must have identical length
        if s.__len__() != t.__len__():
            return False

        dictionary = dict()

        # Initialize character frequency map for all lowercase English letters
        chars = "abcdefghijklmnopqrstuvwxyz"
        for char in chars:
            dictionary[char] = 0

        # Increment counts for string s, decrement for string t
        for char in s:
            dictionary[char] += 1

        for char in t:
            dictionary[char] -= 1

        # If strings are anagrams, every character frequency should balance to 0
        for key in dictionary.keys():
            if dictionary[key] != 0:
                return False

        return True
