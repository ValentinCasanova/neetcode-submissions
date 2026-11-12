class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position, speed), key=lambda x: x[0])
        next_car = fleet = 0
        for pos, speed in cars[::-1]:
            if not (next_car > 0 and next_car >= (target - pos) / speed):
                fleet += 1
                next_car = (target - pos) / speed
        return fleet
