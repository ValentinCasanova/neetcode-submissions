class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pos_speed = sorted(zip(position, speed), key=lambda x: x[0])
        fleet = []
        for car in pos_speed[::-1]:
            arrival = (target - car[0]) / car[1]
            if not fleet:
                fleet.append(arrival)
            else:
                if arrival <= fleet[-1]:
                    continue
                else:
                    fleet.append(arrival)
        return len(fleet)