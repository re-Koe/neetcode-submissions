class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ""
        res = ""
        for word in strs:
            res += str(len(word)) + "#" + word
        return res


    def decode(self, s: str) -> List[str]:
        # 4#word3#cat
        if s == "":
            return []
        res = []
        i = 0

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