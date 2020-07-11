class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0
        le=len(beginWord)
        all=defaultdict(list)
        for word in wordList:
            for i in range(le):
                all[word[:i]+"*"+word[i+1:]].append(word)
        queue=[(beginWord,1)]
        vitised={beginWord:True}
        while queue:
            cur,level=queue.pop(0)
            for i in range(le):
                inter=cur[:i]+"*"+cur[i+1:]
                for word in all[inter]:
                    if word==endWord:
                        return level+1
                    if word not in vitised:
                        vitised[word]=True
                        queue.append((word,level+1))
                all[inter]=[]
        return 0