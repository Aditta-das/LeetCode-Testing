class Solution(object):
    def mergeSort(self, new_list):
        if len(new_list) > 1:
            mid = len(new_list) // 2
            left = new_list[:mid]
            right = new_list[mid:]
            self.mergeSort(left)
            self.mergeSort(right)
            i=j=k=0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    new_list[k] = left[i]
                    i+=1
                else:
                    new_list[k] = right[j]
                    j+=1
                k+=1
            while i < len(left):
                new_list[k] = left[i]
                i+=1
                k+=1
            while j < len(right):
                new_list[k] = right[j]
                j+=1
                k+=1

        return new_list

    def findMedianSortedArrays(self, nums1, nums2):
        new = nums1 + nums2
        if len(new) > 1: 
            new_list = self.mergeSort(new)
            mid = len(new_list)
            if mid % 2 == 0:
                return float(new_list[int(mid/2)] + new_list[int(mid/2)-1]) / 2.0 
            return float(new_list[int(mid/2)])
        else:
            if len(nums1) == 0:
                return float("".join([str(s) for s in nums2]))
            return float("".join([str(s) for s in nums1]))

        

nums1 = [1, 3]
nums2 = [2]
a = Solution()
print(a.findMedianSortedArrays(nums1, nums2))
