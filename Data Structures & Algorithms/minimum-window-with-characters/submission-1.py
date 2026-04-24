class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if t == "": return ""

        needLookup = Counter(t)
        need, have = len(needLookup), 0
        window = defaultdict(int)
        out = ""
        outLength = float('inf')

        l = 0
        for r, curr in enumerate(s):
            # update the window
            window[curr]+=1

            # if we needed this character and we just satisfied a letter count
            if curr in needLookup and window[curr] == needLookup[curr]:
                have += 1

            # while we have all characters, move the left pointer to decrease
            while have == need:
                cand = s[l:r+1]
                if len(cand) < outLength:
                    out = cand
                    outLength = len(cand)
                window[s[l]] -= 1

                if s[l] in needLookup and window[s[l]] < needLookup[s[l]]:
                    have -= 1
                l += 1

            
        return out

        