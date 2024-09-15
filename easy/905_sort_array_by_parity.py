import collections
class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        a = collections.deque()
        for i in nums:
            if i%2==0:
                a.appendleft(i)
            else:
                a.append(i)
        return a