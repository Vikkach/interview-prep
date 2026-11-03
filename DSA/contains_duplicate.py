# Pattern: hash map. If a number is already in the set, return True. O(n) time, O(n) space
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums_dict = dict()
        for n in nums:
            if nums_dict.get(n):
                return True
            nums_dict[n] = 1
        return False
        

a = Solution()
assert a.hasDuplicate([10, 20, 32]) == False
assert a.hasDuplicate([]) == False
assert a.hasDuplicate([2, 4, 0, 0]) == True
assert a.hasDuplicate([-3, -3, -1, 4]) == True
