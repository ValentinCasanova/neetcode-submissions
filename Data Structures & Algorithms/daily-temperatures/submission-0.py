class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        stack = []
        for index, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                i = stack.pop()[0]
                res[i] = index -i
            stack.append([index, temp])
        return res