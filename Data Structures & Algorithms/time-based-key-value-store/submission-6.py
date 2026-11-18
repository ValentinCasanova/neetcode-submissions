class TimeMap:

    def __init__(self):
        self.key_list = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key in self.key_list:
            self.key_list[key].append((timestamp, value))
        else:
            self.key_list[key] = [(timestamp, value)]


    def get(self, key: str, timestamp: int) -> str:
        if not key in self.key_list:
            return ""
        
        cur = self.key_list[key]
        l, r = 0, len(cur) - 1
        res = ''
        while l <= r:
            mid = (l + r) // 2
            if cur[mid][0] > timestamp:
                r = mid - 1
            else:
                if cur[mid][0] <= timestamp:
                    res = cur[mid][1]
                l = mid + 1
        
        return res

