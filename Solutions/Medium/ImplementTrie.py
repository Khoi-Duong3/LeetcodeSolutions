class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_a_word = False

class PrefixTree:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()

            node = node.children[char]
        
        node.is_a_word = True

    def search(self, word: str) -> bool:
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        
        return node.is_a_word
            

    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for char in prefix:
            if char not in node.children:
                return False
            
            node = node.children[char]
        
        return True
        
        