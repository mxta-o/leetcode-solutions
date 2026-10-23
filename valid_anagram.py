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
# this algorithm is O(nlogn) because of the .sort() method
# there is an O(n) runtime for converting the strings to lists
# and O(n) for the loop comparing the chars but in
# practice you usually simplify to the fastest growing term

# optimized solution
# establish a hashmap
# storing all of string s's chars in the hashmap
# and removing those values by 1 if char at t is present
# hmm

class Solution:
    def isAnagram(self, s:str, t:str) -> bool:
        if(len(s) != len(t)):
            return False

        maps = {}
        for char in s:
            if char not in maps:
                maps[char] = 1
            else:
                maps[char] += 1

        for char in t:
            if char in maps:
                maps[char] -= 1
            else:
                return False

        # so for each value in the hasmap
        # if that value is not zero then return False
        for value in maps.values():
            if value != 0:
                return False
        return True

# im ngl its not even implementing the hashmap that gave me cancer
# its returning the result that gives me cancer
# but anyways this solution would be O(n)
# since youre iterating throughout the strings only once
# even though there are three loops, coefficients are negligible