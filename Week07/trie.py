class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = defaultdict()


    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: None
        """
        tree = self.root
        for w in word:
            if w not in tree:
                tree[w] = defaultdict()
            tree = tree[w]
        tree['#'] = '#'




    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        tree = self.root
        for w in word:
            if w not in tree:
                return False
            tree = tree[w]
        if '#' not in tree:
            return False
        return True
            
        


    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        tree = self.root
        for w in prefix:
            if w not in tree:
                return False
            tree = tree[w]
        return True



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)