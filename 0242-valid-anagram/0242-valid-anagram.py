class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
            
        count_s, count_t = {}, {}
        
        for i in range(len(s)):
            count_s[s[i]] = count_s.get(s[i], 0) + 1
            count_t[t[i]] = count_t.get(t[i], 0) + 1
            
        return count_s == count_t

"""
The below solution has same logic as above just the  for loop is split for easier understanding

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len[s] != len[t]:
            return False

        count_s, count_t = {}, {}

        for letter in s:
            if letter in count_s: 
                count_s[letter] += 1 #Already seen so increase its count
            else:
                count_s[letter] = 1 #Seeing it for the first time
        
        for letter in t:
            if letter in count-t:
                count_t[letter] += 1 #Already seen so increase its count
            else:
                count_t[letter] =1 #seeing it for the first time
        
        return count_s == count_t
"""

        