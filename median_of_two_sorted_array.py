class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        a, b = nums1, nums2
        total = len(a) + len(b)
        half = total // 2
        if len(a) > len(b):
            a, b = b, a 
        l, r = 0, len(a) - 1
        while True:
            i = (l + r) // 2 # a
            j = half - i - 2 # b

            aleft = a[i] if i >= 0 else float("-infinity")
            aright = a[i + 1] if (i+1) < len(a) else float("infinity")
            bleft = b[j] if j >= 0 else float("-infinity")
            bright = b[j + 1] if (j+1) < len(b) else float("infinity")

            if aleft <= bright and bleft <= aright:
                # odd
                if total % 2:
                    return min(aright, bright)
                #even
                return (max(aleft, bleft) + min(aright, bright)) / 2
            elif aleft > bright:
                r = i - 1 
            else:
                l = i + 1

nums1 = [1,2]
nums2 = [3,4]

a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))