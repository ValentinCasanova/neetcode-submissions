class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])
        next_car = 0
        fleet = 0
        for pos, speed in cars[::-1]:
            cur_arrival_time = (target - pos) / speed
            if next_car > 0 and next_car >= cur_arrival_time:
                continue
            else:
                fleet += 1
                next_car = cur_arrival_time
        return fleet
