class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        max_time = 0
        fleets = 0
        for place, velocity in cars:
            time = (target - place) / velocity
            if time > max_time:
                fleets += 1
                max_time = time
        return fleets



