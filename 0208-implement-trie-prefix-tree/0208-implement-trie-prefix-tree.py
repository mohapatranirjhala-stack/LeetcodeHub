class TrieNode(object):
    def __init__(self):
        # Maps a character to its corresponding TrieNode
        self.children = {}
        # True if this node represents the end of a complete word
        self.is_end = False


class Trie(object):

    def __init__(self):
        """
        Initializes the trie object.
        """
        self.root = TrieNode()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """
        Returns true if the string word is in the trie, and false otherwise.
        :type word: str
        :rtype: bool
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def startsWith(self, prefix):
        """
        Returns true if there is a previously inserted string word 
        that has the prefix, and false otherwise.
        :type prefix: str
        :rtype: bool
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return False
            node = node.children[char]
        return True