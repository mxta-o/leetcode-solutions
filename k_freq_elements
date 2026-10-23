# input is a list of ints
# as well as an int k
# we must return a list of ints
# that are the most frequent in nums

# initial brute force
# implement a hashmap that stores each num as a key 
# where the value is its frequency count
# and return k number of keys of the highest counts

class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        if len(nums) == 0:
            return []

        maps = {}
        result = []
        for num in nums:
            if num not in maps:
                maps[num] = 1
            else:
                maps[num] += 1

        # we're returning the key of the most frequent elements of size k
        # how can we rank the keys by count tho thinking emoji


        while len(result) < k:
            best_count = 0
            best_key = 0
            # maps.items() turns pairs into (x, y) instead of x: y
            for key, value in maps.items():
                if value > best_count:
                    best_count = value
                    best_key = key
            result.append(best_key)
            # remove key from hashmap so it doesnt win twice
            maps.pop(best_key)
        return result

    # the runtime of this algorithm has a couple of things to account for:
    # hashmap loop: O(n)
    # finding top k elems: O(k * m), such that k is the return elements and
    # m is the unique elements, aka the keys since youre going over
    # all of the keys k amount of times

    # so therefore the runtime of this algo is O(n + k * m) which is not bad kid