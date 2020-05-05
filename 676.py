class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.look={}

    def buildDict(self, dict: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for word in dict:
            tree=self.look
            for a in word:
                if a not in tree:
                    tree[a]={}
                tree=tree[a]
            tree["#"]="#"

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        le=len(word)
        for i in range(le):
            tree=self.look
            for j in range(le):
                if i!=j:
                    if word[j] not in tree:
                        break
                    else:
                        tree=tree[word[j]]
                else:
                    if (len(tree)==1 and "#" in tree) or (len(tree)==2 and "#" in tree and word[j] in tree):
                        break
                    for w in tree:
                        if w!=word[j] and w!="#" and self.sea(word[j+1:],tree[w]):
                            return True
                    break
        return False
    def sea(self,word:str,w):
        for a in word:
            if a not in w:
                return False
            w=w[a]
        if "#" in w:
            return True
        return False

# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)