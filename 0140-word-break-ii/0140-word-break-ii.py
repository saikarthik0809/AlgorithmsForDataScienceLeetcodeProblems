class Tree:
    def __init__(self, end=False):
        self.end = end
        self.children = {}


def get_end(root, word, index):
    node = root
    while node.children and index < len(word):
        if word[index] not in node.children:
            break
        node = node.children[word[index]]
        index += 1
        if node.end:
            yield index

def fill_tree(words):
    root = Tree()
    for word in words:
        node = root
        for char in word:
            if char not in node.children:
                node.children[char] = Tree()
            node = node.children[char]
        node.end = True
    return root


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        root = fill_tree(wordDict)
        stack = []
        result = []
        for i in get_end(root, s, 0):
            stack.append((i, s[:i]))
        while stack:
            index, tmp = stack.pop()
            if index == len(s):
                result.append(tmp)
                continue
            for i in get_end(root, s, index):
                stack.append((i, tmp + " " + s[index:i]))
        return result