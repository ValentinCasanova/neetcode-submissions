class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(zip(position, speed), key=lambda x: x[0])
        highway = []
        for car in reversed(position_speed):
            # Reach target at: (target - position) / speed 
            arrival_time = (target - car[0]) / car[1]
            if not highway:
                highway.append(arrival_time)
            else:
                last_fleet = highway[-1]
                if arrival_time > last_fleet:
                    highway.append(arrival_time)
        return len(highway)
