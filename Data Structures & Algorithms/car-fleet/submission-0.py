class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = sorted(zip(position, speed), reverse=True)
        fleets = 0
        maxTime = 0.0

        for p, s in pair:
            time = (target - p) / s
            if time > maxTime:
                fleets += 1
                maxTime = time
            
        return fleets