class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        numbers = {}
        for i in range(len(nums)):
            if nums[i] in numbers:
                prev_index = numbers[nums[i]]
                if i - prev_index <= k:
                    return True
            numbers[nums[i]] = i
        return False