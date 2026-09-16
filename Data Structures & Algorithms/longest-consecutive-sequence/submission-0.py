class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0

        for number in numSet:
            if (number-1) not in numSet:
                length = 1
                while (number+length) in numSet:
                    length += 1
                res = max(length, res)
        return res
            