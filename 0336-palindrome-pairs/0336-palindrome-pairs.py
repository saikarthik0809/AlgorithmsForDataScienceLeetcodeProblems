class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        pos = {word: i for i, word in enumerate(words)}
        ans = set()
        for i, word in enumerate(words):
            if not word: continue
            L = len(word)
            flipped = word[::-1]
            for offset in range(0, L+1):
                if word[offset:L] == flipped[0:L-offset]:
                    if (compl := flipped[L-offset:]) in pos and pos[compl]!=i:
                        ans.add((i, pos[compl]))
                if flipped[offset:L] == word[0:L-offset]:
                    if (compl := flipped[0:offset]) in pos and pos[compl]!=i:
                        ans.add((pos[compl], i))
        return list(map(list, ans))