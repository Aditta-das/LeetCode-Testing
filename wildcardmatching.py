class Solution(object):
    def isMatch(self, s, p):
        if s == p:
            return True
        mat = []
        [mat.append([False]*(len(s)+1)) for _ in range(len(p)+1)]
        mat[0][0] = True
        for i in range(0, len(p)):
            c = p[i]
            if c == "*":
                mat[i+1][0] = mat[i][0]

        for i in range(len(p)):
            for j in range(len(s)):
                c1 = s[j]
                c2 = p[i]
                if c2 == "*":
                    mat[i+1][j+1] = mat[i][j] or mat[i+1][j] or mat[i][j+1]
                elif c2 == "?":
                    mat[i+1][j+1] = mat[i][j]
                else:
                    mat[i+1][j+1] = mat[i][j] and (c1 == c2)
        return mat[len(p)][len(s)]


s = "adceb"
p = "*a*b"
a = Solution()
print(a.isMatch(s, p))