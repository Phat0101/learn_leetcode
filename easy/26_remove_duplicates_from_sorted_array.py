class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        index = 0
        seen = -1000
        for i in nums:
            if i != seen:
                nums[index] = i
                seen=i
                index+=1
        return index
        