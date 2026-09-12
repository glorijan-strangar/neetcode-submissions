class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for number in nums:
            counter[number] = counter.get(number, 0) + 1
        return [item[0] for item in sorted(counter.items(), key = lambda item: item[1], reverse = True)[:k]]