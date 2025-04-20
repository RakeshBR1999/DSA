# Trie Node
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

# Time Complexity:
# - Insert: O(M), where M is the length of the word
# - Search: O(M), where M is the length of the word
# - Starts With: O(M), where M is the length of the prefix
# Space Complexity: O(N), where N is the number of nodes in the trie


# Trie Implementation
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True
    
    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word
    
    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True

# Usage
trie = Trie()
trie.insert("cat")
trie.insert("cap")
trie.insert("can")

print(trie.search("cat"))      # True
print(trie.search("cab"))      # False
print(trie.starts_with("ca"))  # True
print(trie.starts_with("dog")) # False

# print the tree structure
def print_trie(node, prefix=""):
    if node.is_end_of_word:
        print(prefix)
    for ch, child_node in node.children.items():
        print_trie(child_node, prefix + ch)
print("Trie structure:")
print_trie(trie.root)
