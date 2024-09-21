class Solution:
    def makeStringsEqual(self, s: str, target: str) -> bool:
        if (s==target):
            return True
        def check(s:str) -> bool:
            for i in s:
                if i =='1':
                    return False
            return True
        if check(s) or check(target):
            return False
        return True
        # or 
        # return (s == target) or ('1' in s and '1' in target)