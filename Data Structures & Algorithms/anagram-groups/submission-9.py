class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        amap = defaultdict(list) # (1 , ..., 0) : aword

        for word in strs:
            charTup = [0] * 26
            for c in word:
                charTup[ord('a') - ord(c)] += 1
            amap[tuple(charTup)].append(word)
        
        return list(amap.values())