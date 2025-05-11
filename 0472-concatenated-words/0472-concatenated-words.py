class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        res = []
        word_set = set(words)
        incorrect = set()

        def dfs(word):
            if word in word_set:
                return True
            elif word in incorrect:
                return False
            else:
                for i in range(1, len(word)):
                    if word[:i] in word_set:
                        if dfs(word[i:]):
                            return True
                        else:
                            incorrect.add(word[i:])
                incorrect.add(word)
                return False
        
        for word in words:
            word_set.remove(word)
            if dfs(word):
                res.append(word)
            word_set.add(word)
        
        return res