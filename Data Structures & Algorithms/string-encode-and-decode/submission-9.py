class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == "":
            return ""
        
        res = ""
        for s in strs:
            res = res + str(len(s)) + "#" + s
        
        return res



    def decode(self, s: str) -> List[str]:
        "word, word2, try   ---->    4#word5#word23#try"
        if s == "":
            return []

        i = 0
        res = []

        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            res.append(s[i:j])
            i = j
        return res