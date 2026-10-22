# brute force solution
# outer loop iterating with i
# inner loop with j tracking the element after i
# so if i and j are equal then return true
# if not then keep iterating throughout the inner loop
# until the end of the list before i iterates

# runtime of O(n^2) because of a nested for loop

class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                if nums[i] == nums[j]:
                    return True
        return False
        