class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        ans = 0
        not_seen = {}
        for stone in stones:
            if stone in not_seen:
                not_seen[stone] += 1
            else:
                not_seen[stone] = 1

        for jewel in jewels:
            if jewel in not_seen:
                ans += not_seen[jewel]
        return ans

jewels = "aA"
stones = "aAAbbbb"
a = Solution()
print(a.numJewelsInStones(jewels, stones))