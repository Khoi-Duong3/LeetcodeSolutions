class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_a_word = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            
            node = node.children[char]
        
        node.is_a_word = True

    def search(self, word: str) -> bool:
        def dfs(index, root):
            node = root

            for i in range(index, len(word)):
                char = word[i]
                if char == ".":
                    for child in node.children.values():
                        if dfs(i + 1, child):
                            return True
                    return False
                else:
                    if char not in node.children:
                        return False
                    
                    node = node.children[char]
            
            return node.is_a_word
        
        return dfs(0, self.root)
