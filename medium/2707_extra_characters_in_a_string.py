import re
class Solution:
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        n = len(s)
        dp = [float('inf')] * (n+1)
        dp[0] = 0
        words = set(dictionary)
        for i in range(1,n+1):
            dp[i] = dp[i-1]+1
            for j in range(i):
                if s[j:i] in words:
                    dp[i] = min(dp[i], dp[j])
        return dp[n]
