# Pattern: hash map with frequency as key and numbers as values. Time: O(n), Space O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c_hash = dict()
        for n in nums:
            c_hash[n] = c_hash.get(n, 0) + 1
        freq = [[] for i in range(len(nums) + 1)]
        for n, c in c_hash.items():
            freq[c].append(n)
        result = []
        for f in reversed(freq):
            if f != []:
                for i in f:
                    result.append(i)
        return result[:k]
