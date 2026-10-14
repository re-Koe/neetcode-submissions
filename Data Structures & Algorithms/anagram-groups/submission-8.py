class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        charMap = defaultdict(list) # (1, 0, 1, ..., 1, ..., 0) : [act]

        for s in strs:
            letters = [0] * 26
            for char in s:
                letters[ord('a') - ord(char)] += 1
            charMap[tuple(letters)].append(s)
        
        return list(charMap.values())