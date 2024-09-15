class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        length = len(candidates)
        def dq(diff: int, combination: List[int], start: int):
            if diff == 0:
                result.append(combination.copy())
                return
            if diff < candidates[0]:
                return
            for i in range(start, length):
                if candidates[i] > diff:
                    break
                combination.append(candidates[i])
                dq(diff - candidates[i], combination, i)
                combination.pop()
        candidates.sort()
        dq(target, [], 0)
        return result