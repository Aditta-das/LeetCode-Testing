class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        rev = int(str(abs(x))[::-1])
        print(rev)
        return (-rev if x < 0 else rev) if rev.bit_length() < 32 else 0


x = -123
a = Solution()
print(a.reverse(x))