class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.look={}


    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        tree=self.look
        for a in word:
            if a not in tree:
                tree[a]={}
            tree=tree[a]
        tree["#"]="#"

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        tree=self.look
        le=len(word)
        for i in range(le):
            if 'a'<=word[i]<='z' and word[i] not in tree:
                return False
            elif word[i]=='.' and len(tree)==1 and "#" in tree:
                return False
            elif word[i]=='.':
                treefu=WordDictionary()
                for a in tree:
                    treefu.look=tree[a]
                    if treefu.search(word[i+1:]):
                        return True
                return False
            else:
                tree=tree[word[i]]
        if "#" in tree:
            return True
        return False
# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)