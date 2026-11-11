class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0])
        fleets = []
        for pos, speed in pos_speed[::-1]:
            arrival_time = (target - pos) / speed
            if fleets and ((target - fleets[-1][0][0]) / fleets[-1][0][1]) >= arrival_time:
                fleets[-1].append((pos, speed))
            else:
                fleets.append([(pos, speed)])
        return len(fleets)
