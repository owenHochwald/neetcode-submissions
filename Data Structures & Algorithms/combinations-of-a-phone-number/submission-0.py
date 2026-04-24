class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        lookup = {
            "2" : ["a", "b", "c"],
            "3" : ["d", "e", "f"],
            "4" : ["g", "h", "i"],
            "5" : ["j", "k", "l"],
            "6" : ["m", "n", "o"],
            "7" : ["p", "q", "r", "s"],
            "8" : ["t", "u", "v"],
            "9" : ["w", "x", "y", "z"]
        }
        out = []

        def backtrack(i, path):
            if i == len(digits):
                out.append(''.join(path))
                return
            else:
                for combos in lookup[digits[i]]:
                    backtrack(i+1, path + [combos])
        backtrack(0, [])
        return out


        