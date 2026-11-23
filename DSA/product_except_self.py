# Pattern: 2 list with prefix and suffix products. Space: O(n), Time: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref_prod = [0]*len(nums)
        suff_prod = [0]*len(nums)
        res = [0]*len(nums)
        pref_prod[0] = 1
        suff_prod[0] = 1
        
        for i, n in enumerate(nums):
            if i < len(nums)-1:
                pref_prod[i+1] = pref_prod[i]*n

        for j, n in enumerate(reversed(nums)):
            if j < len(nums)-1:
                suff_prod[j+1] = suff_prod[j]*n
        
        for k in range(len(nums)):
            res[k] = pref_prod[k]*suff_prod[len(nums)-1-k]
        return res

        
