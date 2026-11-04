# Pattern: hash map. Store indices and numbers to hashmap, check diff if present. Time: O(n), Space: O(n)
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n_hash = dict()
        for i, n in enumerate(nums):
            n_hash[n] = i
        for i, n in enumerate(nums):
            diff = target - n
            if j := n_hash.get(diff):
                if i != j:
                    return [i, j]
        return []

s = Solution()
assert s.twoSum([1, 2, 3], 4) == [0, 2]
assert s.twoSum([-3, -4], -7) == [0, 1]