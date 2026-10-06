class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = set()
        res, curr = [], []
        for i in range(len(strs)):
            x = i + 1
            if i in grouped:
                continue
            curr = [strs[i]]
            while x < len(strs):
                if sorted(strs[x]) == sorted(strs[i]) and x not in grouped:
                    curr.append(strs[x])
                    grouped.add(x)
                x +=1
            res.append(curr)
        return res


