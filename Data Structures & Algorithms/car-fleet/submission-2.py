class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        position_speed = sorted(list(zip(position, speed)), key=lambda car: car[0])
        stack = []
        for car in reversed(position_speed):
            arrival_time = (target - car[0]) / car[1]
            stack.append(arrival_time)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
