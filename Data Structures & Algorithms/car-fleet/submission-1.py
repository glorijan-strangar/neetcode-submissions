class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        s = []
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        sorted_cars = sorted(cars, key = lambda x: x[0], reverse = True)

        for j in range(len(cars)):
            s.append((target - sorted_cars[j][0])/sorted_cars[j][1])
            if len(s) >= 2 and s[-1] <= s[-2]:
                s.pop(-1)
        return len(s)
            