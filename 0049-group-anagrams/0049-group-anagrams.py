class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to store anagram groups
        anagram_dict = defaultdict(list)

        for word in strs:
            # Sort the word and use it as a key
            sorted_words = tuple(sorted(word))
         # Append the original word to its corresponding anagram group
            anagram_dict[sorted_words].append(word)

        # Return grouped anagrams as a list of lists
        return list(anagram_dict.values())

        