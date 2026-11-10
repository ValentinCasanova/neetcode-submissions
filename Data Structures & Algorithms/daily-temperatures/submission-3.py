class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = [0] * len(temperatures)
        temp = []
        for i in range(len(temperatures) - 1, -1, -1):
            while temp:
                if temp[-1][0] > temperatures[i]:
                    res[i] = temp[-1][1] - i
                    break
                temp.pop()                
            temp.append((temperatures[i], i))
        return res