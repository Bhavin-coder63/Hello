from collections import Counter

class Solution:
    def isAnagram(self, s, t):
        return Counter(s) == Counter(t)


sol = Solution()
print(sol.isAnagram("anagram", "nagaram"))  
print(sol.isAnagram("rat", "car"))          

