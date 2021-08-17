class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        if len(nums1) > len(nums2):
            temp = nums1
            nums1 = nums2
            nums2 = temp
        
        lo = 0
        hi = len(nums1)
        combined = len(nums1) + len(nums2)

        while (lo <= hi):
            partX = (lo + hi) / 2
            partY = (combined + 1) / 2 - partX
            return partX, partY

nums1 = [1, 2]
nums2 = [3, 4]
a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))