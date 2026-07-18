class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        s = []

        for a in asteroids:
            while s and a < 0 < s[-1]: 
                if -a == s[-1]:
                    s.pop()
                elif -a > s[-1]:
                    s.pop()
                    continue
                break
            else:
                s.append(a)
        return s