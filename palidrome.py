class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        x = str(x)
        revs_x = x[::-1]
        if x == revs_x:
            return True
        else:
            return False
        
a = Solution()
print(a.isPalindrome(121))