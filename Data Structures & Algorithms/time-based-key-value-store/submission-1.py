from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.key = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.key[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        time_value = self.key.get(key, "")
        if not time_value:
            return ""
        
        l, r = 0, len(time_value) - 1
        res = ""
        while l <= r:
            mid = l + ((r - l) // 2)
            if time_value[mid][0] <= timestamp:
                res = time_value[mid][1]
                l = mid + 1
            else:
                r = mid -1
        return res