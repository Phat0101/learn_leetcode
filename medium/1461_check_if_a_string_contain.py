class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        se = set()
        for i in range(len(s)-k+1):
            se.add(s[i:i+k])
        if len(se) == 2**k:
            return True
        return False