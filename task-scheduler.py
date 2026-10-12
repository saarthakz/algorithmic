"""
You are given an array of CPU tasks tasks, where tasks[i] is an uppercase english character from A to Z. You are also given an integer n.

Each CPU cycle allows the completion of a single task, and tasks may be completed in any order.

The only constraint is that identical tasks must be separated by at least n CPU cycles, to cooldown the CPU.

Return the minimum number of CPU cycles required to complete all tasks.
"""

from typing import List, Deque, Tuple
import heapq
from collections import Counter, deque


class Solution:
    def leastInterval(self, tasks: List[str], cooldown: int) -> int:
        cooldown_queue: Deque[Tuple[str, int]] = deque()
        scheduling_queue = []

        ctr = Counter(tasks)

        # -1 since Python has a min heap implementation
        scheduling_queue = [(-1 * ctr[task], task) for task in ctr]
        heapq.heapify(scheduling_queue)

        task_ctr = 0

        # While there are tasks to be scheduled
        while len(ctr.keys()):

            # If there are tasks to pick
            if len(scheduling_queue):

                # Get the task with most frequency in the schedule
                task_freq, task = heapq.heappop(scheduling_queue)

                # Decrement it's counter, since it has now been picked up
                ctr[task] -= 1

                # If it is done with, remove it from the counter
                if ctr[task] == 0:
                    ctr.pop(task)

                # If the task is not done
                else:
                    # Add the current task and current task counter (to count the cooldown)
                    cooldown_queue.append((task, task_ctr))

            task_ctr += 1

            # The task counter for the element at the front of the queue
            if len(cooldown_queue) and task_ctr - cooldown_queue[0][1] > cooldown:

                # If the cooldown period is over, add it back to the scheduling queue
                task, _ = cooldown_queue.popleft()
                heapq.heappush(scheduling_queue, (-1 * ctr[task], task))

        return task_ctr
