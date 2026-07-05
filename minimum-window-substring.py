class Solution:

    def executor(self, s: str, t: str) -> tuple[int, int]:
        freq_map_of_t = {}

        # Frequency map of 't'
        for char in t:
            if char in freq_map_of_t:
                freq_map_of_t[char] += 1
            else:
                freq_map_of_t[char] = 1

        # Check if the entire string is 's' is applicable for the given condition or not

        # Create a frequency map of 's' as well
        freq_map_of_s = {}

        for char in s:
            if char in freq_map_of_s:
                freq_map_of_s[char] += 1
            else:
                freq_map_of_s[char] = 1

        for key in freq_map_of_t.keys():
            if key not in freq_map_of_s:
                return (-1, -1)
            if freq_map_of_s[key] < freq_map_of_t[key]:
                return (-1, -1)
            continue

        # Frequency map iteration is always O(26)
        window_freq_map = freq_map_of_t.copy()

        # Returns if all the frequencies in the freq map are zeroes or not
        def is_freq_map_valid(freq_map: dict[str, int]) -> bool:
            for key in freq_map.keys():
                if freq_map[key] > 0:
                    return False

            return True

        left = 0
        right = 0

        min_substring_len = len(s)
        min_substring_tuple = (left, len(s) - 1)

        # Let's first position the left pointer correctly to the first viable character
        while left < len(s):
            if s[left] in freq_map_of_t:
                break
            left += 1

        right = left

        # Now that the left ptr is at the correct location for the first time, we can look at expanding the window
        while right < len(s):

            # Grow the window to the right till you have a valid substring (i.e that freq map is not zeroed)
            if not is_freq_map_valid(window_freq_map):
                curr = s[right]
                if curr in window_freq_map:
                    window_freq_map[curr] -= 1
                right += 1

            # Now that you have a valid substring, cut the window short, till
            else:
                curr_length = right - left

                if curr_length < min_substring_len:
                    min_substring_len = curr_length
                    min_substring_tuple = (left, right - 1)

                # Now let's remove the left character from the window and find the new left
                window_freq_map[s[left]] += 1

                left += 1

                while left < right and is_freq_map_valid(window_freq_map):
                    curr_length = right - left
                    if curr_length < min_substring_len:
                        min_substring_len = curr_length
                        min_substring_tuple = (left, right - 1)
                    curr_char = s[left]
                    if curr_char in window_freq_map:
                        window_freq_map[curr_char] += 1
                    left += 1

                while left < right and s[left] not in window_freq_map:
                    left += 1

                # Now the new left is set, we can again start increasing window

        if is_freq_map_valid(window_freq_map):
            curr_length = right - left
            if curr_length < min_substring_len:
                min_substring_len = curr_length
                min_substring_tuple = (left, right - 1)

        return min_substring_tuple

    def minWindow(self, s: str, t: str) -> str:

        ans_tuple = self.executor(s, t)
        ans_tuple_s_reversed = self.executor(s[::-1], t)
        ans_tuple_s_reversed_corrected = (
            len(s) - (ans_tuple_s_reversed[1] + 1),
            len(s) - (ans_tuple_s_reversed[0] + 1),
        )

        if ans_tuple == ans_tuple_s_reversed == (-1, -1):
            return ""

        l1, r1 = ans_tuple
        l2, r2 = ans_tuple_s_reversed_corrected

        if r1 - l1 < r2 - l2:
            return s[l1 : r1 + 1]
        else:
            return s[l2 : r2 + 1]
