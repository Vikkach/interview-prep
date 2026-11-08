# Pattern: hash map with key as sorted letters and value as string. Time: O(n*klogk), Space: O(n*k)
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # key - sorted letters of str
        # value - string from list
        if strs == []:
            return [] 
        s_hash = dict()
        for s in strs:
            sort_str = "".join(sorted(s))
            s_hash[sort_str] = s_hash.get(sort_str, [])
            s_hash[sort_str].append(s)
        result = [v for k, v in s_hash.items()]
        return result

s = Solution()
assert s.groupAnagrams(["str", "tsr", "abc"]) == [["str", "tsr"], ["abc"]]
assert s.groupAnagrams([""]) == [[""]]

        
        
