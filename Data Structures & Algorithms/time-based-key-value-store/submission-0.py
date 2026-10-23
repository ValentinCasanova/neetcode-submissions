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
        while l <= r:
            mid = l + ((r - l) // 2)
            if time_value[mid][0] == timestamp:
                return time_value[mid][1]
            elif time_value[mid][0] > timestamp:
                r = mid - 1
            else:
                l = mid + 1
        if l - 1 > -1 and time_value[l - 1][0] <= timestamp:
            return time_value[l - 1][1]
        return ""