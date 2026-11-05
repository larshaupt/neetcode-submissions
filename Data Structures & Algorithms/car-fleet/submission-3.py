class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        n_fleets = n
        cars = sorted(zip(position, speed))
        next_car = cars[n-1]
        for i in range(n-2, -1, -1):
            car = cars[i]
            rel_speed = car[1] - next_car[1]
            rel_diff = next_car[0] - car[0]
            if rel_speed > 0 and rel_diff/rel_speed <= (target-next_car[0])/next_car[1]:
                # car catches up
                n_fleets -= 1
            else:
                next_car = car

        return n_fleets

        
