class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        unique = set()
        curr = 0
        longest = curr
        left = 0
        for i in range(len(s)):
            if s[i] not in unique:
                unique.add(s[i])
                curr += 1
            else:
                while s[i] in unique:
                    unique.remove(s[left])
                    left += 1
                    curr -= 1
                unique.add(s[i])
                curr += 1
            longest = max(curr, longest)

        return longest

