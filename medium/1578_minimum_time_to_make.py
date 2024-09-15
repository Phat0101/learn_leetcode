class Solution:
    def minCost(self, colors: str, neededTime: List[int]) -> int:
        total_cost = 0
        n = len(colors)
        for i in range(1, n):
            if colors[i] == colors[i - 1]:
                total_cost += min(neededTime[i], neededTime[i - 1])
                neededTime[i] = max(neededTime[i], neededTime[i - 1])
        return total_cost
