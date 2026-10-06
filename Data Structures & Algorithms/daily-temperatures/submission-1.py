class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for _ in temperatures]
        stack = []
        for idx, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                warmer_day = stack.pop()
                res[warmer_day[0]] = idx - warmer_day[0]
            stack.append((idx, temp))
        return res
        