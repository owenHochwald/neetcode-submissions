class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        out = 0 

        l, r = 0, len(people) - 1

        while l <= r:
            curr = people[r]
            r -= 1

            if l <= r and people[l] + curr <= limit:
                l += 1
            out += 1
                

        


        return out


