# Pattern: set of numbers. check if element is a start of the streak, look for the next +1 element. Space: O(n), Time O(n)
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        current_streak = 0
        curr = 0
        max_streak = 0
        for n in set_nums:
            if (n - 1) not in set_nums:
                current_streak = 1
                curr = n
                while (curr + 1) in set_nums:
                    curr += 1
                    current_streak += 1
                if current_streak > max_streak:
                    max_streak = current_streak
        return max_streak
