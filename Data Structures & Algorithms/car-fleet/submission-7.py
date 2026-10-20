class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0], reverse=True)
        fleet = []
        for car in pos_speed:
            arrival = (target - car[0]) / car[1]
            if fleet and arrival <= fleet[-1]:
                continue
            fleet.append(arrival)
        return len(fleet)