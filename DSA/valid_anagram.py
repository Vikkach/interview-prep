# Pattern: hash set, count number for each letter and compare. Time O(n+m), space O(1)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        def st_to_hash(st):
            h = dict()
            for i in st:
                h[i] = h.get(i, 0) + 1
            return h
        return st_to_hash(s) == st_to_hash(t)

s = Solution()
assert s.isAnagram("a", "a") == True
assert s.isAnagram("a", "b") == False
assert s.isAnagram("bcd", "cdb") == True
assert s.isAnagram("acd", "cdb") == False