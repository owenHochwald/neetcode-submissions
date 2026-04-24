class Solution:
    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            count = str(len(s))
            curr = count + "[" + s
            res += curr
        return res


    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        num = 0
        while i < len(s):
            if s[i].isdigit():
                num = num * 10 + int(s[i])
                i += 1
            elif s[i] == '[':
                res.append(s[i+1:i+num+1])
                i+= (num+1)
                num = 0
            else:
                i += 1
        return res
            

