"""
Design a time-based key-value data structure that can store multiple values for the same key at different time stamps and retrieve the key's value at a certain timestamp.

Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev. If there are no values, it returns "".

"""

from typing import List, Dict, Tuple
import bisect

class TimeMap:

    def __init__(self):
        # For any given key, 
        # We will store a sorted timestamp list and the value mapped to that timestamp
        self.map: Dict[str, Tuple[List[int], Dict[int, str]]] = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.map:
            ts_arr = [timestamp] # Timestamp list
            ts_mapping = { timestamp: value } # Timestamp mapping 
            self.map[key] = (ts_arr, ts_mapping)
            return

        ts_arr, ts_mapping = self.map[key]

        # Get the insertion index in the timestamp list
        ins_idx = bisect.bisect(ts_arr, timestamp)
        ts_arr.insert(ins_idx, timestamp)

        # Add the timestamp mapping
        ts_mapping[timestamp] = value

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.map:
            return ""

        ts_arr, ts_mapping = self.map[key]

        # Get the timestamp index (Closest or actual)
        idx = bisect.bisect(ts_arr, timestamp)

        print(idx, len(ts_arr))

        # If the timestamp is greater than any that exists in the store
        # Measured by the index in the timestamp list
        if idx == len(ts_arr):
            # Return the value at the greatest existing timestamp
            return ts_mapping[ts_arr[idx - 1]]

        # For other indices

        # If the timestamp matches, return the value as is
        if ts_arr[idx] == timestamp:
            return ts_mapping[ts_arr[idx]]

        # 0th index and no value match means previous timestamp also won't exist
        if idx == 0:
            return ""
        
        # The timestamp does not match, hence return the just previous one
        return ts_mapping[ts_arr[idx - 1]]
