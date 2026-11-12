# Pattern: product for all non-zero numbers and division. Time: O(n), Space: O(n)
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output = [0]*len(nums)
        zero_mult = 0
        zero_count = 0
        def mult(lst):
            result = lst[0]
            for l in lst[1:]:
                result = result*l
            return result

        for i, n in enumerate(nums):
            if n == 0:
                zero_count += 1
                if zero_count >= 2:
                    return output
                sublist = nums.copy()
                sublist.remove(0)
                zero_mult = mult(sublist)
                output[i] = zero_mult
                return output

        all_mult = mult(nums)

        for i, n in enumerate(nums):
            output[i] = int(all_mult/n)
        return output

        
