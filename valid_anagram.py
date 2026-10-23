# brute force solution
# turn the strings of s and t into a list
# to sort them alphebetically
# and if the s char at i is equal to the t char at j
# then remove them from the list
# so if theyre both empty then its true
# if theyre not the same char then immediately throw false
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if(len(s) != len(t)):
            return False
        list_s = list(s)
        list_t = list(t)

        list_s.sort()
        list_t.sort()

        for char in range(len(list_s)):
            if list_s[char] != list_t[char]:
                return False
        return True
        