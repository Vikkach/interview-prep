# Pattern: preprocess string, move 2 pointers from head/tail and compare. Time: O(n), Space: O(n)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        post_str = ""
        for c in s:
            if c.isdigit() or c.isalpha():
                post_str += c.lower()

        l = len(post_str)
        for i in range(l):
            if post_str[i] != post_str[l-1-i]:
                return False
        return True 
            
        
