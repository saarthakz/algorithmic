"""
You are given an array of integers candidates, which may contain duplicates, and a target integer target. Your task is to return a list of all unique combinations of candidates where the chosen numbers sum to target.

Each element from candidates may be chosen at most once within a combination. The solution set must not contain duplicate combinations.

You may return the combinations in any order and the order of the numbers in each combination can be in any order.
"""

from typing import List, Set


class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        self.ans = []
        candidates.sort()
        selected_indices = []
        self.helper(
            candidates=candidates,
            target=target,
            path=selected_indices,
            curr_idx=0,
        )

        return [list(comb) for comb in self.ans]

    def helper(
        self, candidates: List[int], target: int, path: List[int], curr_idx: int
    ):
        # Target achieved
        if target == 0:
            self.ans.append(path.copy())
            return

        # Index out of bounds
        if curr_idx == len(candidates):
            return

        # If the candidate at the current index is larger than the target, forget it and return
        if candidates[curr_idx] > target:
            return

        # Current candidate is less than or equal to target

        # Include the current candidate.
        path.append(candidates[curr_idx])
        self.helper(candidates, target - candidates[curr_idx], path, curr_idx + 1)
        path.pop()

        # Exclude this candidate and all identical copies.
        next_idx = curr_idx + 1

        while (
            next_idx < len(candidates) and candidates[next_idx] == candidates[curr_idx]
        ):
            next_idx += 1

        self.helper(candidates, target, path, next_idx)
        return
