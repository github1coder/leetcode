class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        se=set(wordList)
        if not endWord in se:
            return []
        def edges(word):
            arr=list(word)
            for i in range(len(arr)):
                c=arr[i]
                for j in range(97,123):
                    arr[i]=chr(j)
                    newWord=''.join(arr)
                    if newWord in se and not newWord in marked:
                        yield newWord
                arr[i]=c
        res=[]
        marked=set()
        queue=[[beginWord]]
        while queue:
            temp=[]
            found=False
            for words in queue:
                marked.add(words[-1])
            for words in queue:
                for w in edges(words[-1]):
                    v=words+[w]
                    if w == endWord:
                        res.append(v)
                        found=True
                    temp.append(v)
            if found:          
                break
            queue=temp
        return res