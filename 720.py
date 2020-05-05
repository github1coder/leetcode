class Solution:
    def longestWord(self, words: List[str]) -> str:
        res=''
        trie=Tire()
        for word in words:
            trie.insert(word)
        for word in words:
            if trie.search(word):
                if len(word)> len(res):
                    res=word
                elif len(word)==len(res) and word<res:
                    res=word
        return res
    
class Tire:
    def __init__(self):
        self.lookup={}
    
    def insert(self,word:str):
        tree=self.lookup
        for a in word:
            if a not in tree:
                tree[a]={}
            tree=tree[a]
        tree["#"]="#"

    def search(self,word:str)->bool:
        tree=self.lookup
        for a in word:
            if "#" not in tree[a]:
                return False
            tree=tree[a]
        return True
