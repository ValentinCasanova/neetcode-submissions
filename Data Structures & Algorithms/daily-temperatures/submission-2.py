class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0 for i in range(len(temperatures))]
        mon_stack = []
        for i in range(len(temperatures)):
            while mon_stack and temperatures[i] > temperatures[mon_stack[-1]]:
                index = mon_stack.pop()
                res[index] = i - index
            mon_stack.append(i)
        return res