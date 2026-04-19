class Solution:

    def encode(self, strs: List[str]) -> str:
        finStr = ""
        for astr in strs:
            finStr += str(len(astr)) + "#" + astr
        return finStr

    def decode(self, s: str) -> List[str]:
        listy = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            length = int(s[i:j])
            i = j + 1
            j = i + length
            listy.append(s[i:j])
            i = j
        
        return listy 