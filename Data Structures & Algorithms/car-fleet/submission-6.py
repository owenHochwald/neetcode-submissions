class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        count = 1

        first = (target - cars[0][0]) / cars[0][1]
        stack = [first]
        for c in cars[1:]:
            curr = (target - c[0]) / c[1]
            print(curr)
            if (stack and stack[-1] < curr):
                count += 1
                stack.append(curr)

        return len(stack)

