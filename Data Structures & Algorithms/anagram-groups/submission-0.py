class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        main = {}
        for s in strs:
            sig = self.get_signature(s)
            if sig not in main:
                main[sig] = []
            main[sig].append(s)
        return list(main.values())

    def get_signature(self, word: str) -> tuple:
        count = [0] * 26
        for char in word:
            count[ord(char) - ord('a')] += 1
        return tuple(count)