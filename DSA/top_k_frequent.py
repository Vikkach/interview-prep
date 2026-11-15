# Pattern: hash map with frequency as key and numbers as values. Time: O(n), Space O(n)

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if not nums:
            return []
        el_freq_hash = dict()
        for n in nums:
            el_freq_hash[n] = el_freq_hash.get(n, 0) + 1

        n_freq = max(el_freq_hash.values()) + 1
        freq_list = [[] for _ in range(n_freq)]

        for el, c in el_freq_hash.items():
            stored_els = freq_list[c]
            stored_els.append(el)
            freq_list[c] = stored_els
        result = []
        freq_list.reverse()
        for f in freq_list:
            for i in f:
                result.append(i)
        return result[:k]







            




                

        
