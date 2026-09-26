class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        CharToWord = defaultdict(list) # (0 ... 0) : [words]

        for word in strs:
            count = [0] * 26
            for char in word:
                count[ord(char) - ord('a')] += 1
            CharToWord[tuple(count)].append(word)
        return list(CharToWord.values())
