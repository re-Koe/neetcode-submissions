class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = defaultdict(list) # (0, ..., 0), actual word

        for i in strs:
            letterCnt = [0] * 26
            for j in i:
                letterCnt[ord(j) - ord('a')] += 1
            amap[tuple(letterCnt)].append(i)
        return list(amap.values())