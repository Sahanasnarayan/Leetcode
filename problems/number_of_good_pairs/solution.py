class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        repeat = {}
        count = 0
        for value in nums:
            # if value is in hashmap
            if value in repeat:
                if repeat[value] == 1:
                    count += 1
                    # if value is in hashmap and its count being more than 2
                else:
                    count += repeat[value]
                repeat[value] += 1
                # if value is not in hashmap , just add it to hashmap
            else:
                repeat[value] = 1
        return count