class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        current_sum = 0
        smallest_length = n + 1
        for right in range(n):
            current_sum += nums[right]
            while current_sum >= target:
                smallest_length = min(smallest_length, right - left + 1)
                current_sum -= nums[left]
                left += 1
        return smallest_length if smallest_length <= n else 0