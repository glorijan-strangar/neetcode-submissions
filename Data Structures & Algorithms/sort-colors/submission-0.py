class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counts = [0, 0, 0]
        i = 0
        for n in nums:
            if n == 0:
                counts[0] += 1
            elif n == 1:
                counts[1] += 1
            else:
                counts[2] += 1
        while i < len(nums):
            for _ in range(counts[0]):
                nums[i] = 0
                i += 1
            for _ in range(counts[1]):
                nums[i] = 1
                i += 1
            for _ in range(counts[2]):
                nums[i] = 2
                i += 1
