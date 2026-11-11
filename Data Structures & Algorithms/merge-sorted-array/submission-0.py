class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        pt1 = m
        pt2 = 0
        while pt1 < (m+n):
            nums1[pt1] = nums2[pt2]
            pt1 += 1
            pt2 += 1
        nums1.sort()