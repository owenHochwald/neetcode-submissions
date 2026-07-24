class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        hand.sort()
        used = [False] * len(hand)

        start = 0
        n = len(hand) // groupSize
        for _ in range(n):
            while start < len(hand) and used[start]:
                start += 1
            if start == len(hand):
                return False

            used[start] = True
            curr = hand[start]
            search = start + 1

            for _ in range(groupSize-1):
                while search < len(hand):
                    if not used[search] and hand[search] == curr + 1:
                        used[search] = True
                        curr = hand[search]
                        search += 1
                        break
                    search += 1
                else:
                    return False
        return True
            
        