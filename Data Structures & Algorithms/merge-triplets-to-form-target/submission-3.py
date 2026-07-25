class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        # if multiple different elements that match target[i] pick the one with the smallest other elements
        # if picking an element makes the max of any of the elements more than target, return false

        # if any triplet has a value larger than any of the target values, we can remove that triplet
        # then we can collapse all of the triplets to find if the end equals target

        # removing from the list could be expensive and its possible we could do it in O(n) extra space
        
        good = []

        for tri in triplets:
            over = False
            for i, v in enumerate(tri):
                if v > target[i]:
                    over = True 
            if not over:
                good.append(tri)
        
        print(good)

        if good and [
           max([tri[0] for tri in good]),
           max([tri[1] for tri in good]),
           max([tri[2] for tri in good])
        ] == target:
            return True
        return False