class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        counts = {}
        maj = None
        for num in nums:
            if num in counts:
                counts[num] += 1
                continue
            counts[num] = 0
        for num in nums:
            if maj is None:
                maj = num
            if counts[num] > counts[maj]:
                maj = num
        return maj

            
