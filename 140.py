class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordset=set(wordDict)
        dp=[False]*len(s)
        record=defaultdict(list)
        ans=[]
        for i in range(len(s)):
            for j in range(i+1):
                w=s[j:i+1]
                if (j<1 or dp[j-1]) and w in wordset:
                    dp[i]=True
                    record[i].append(j)
        def dfs(i,path):
            if i<=0:
                ans.append(path[:-1])
                return
            for val in record[i-1]:
                dfs(val,s[val:i]+" "+path)
        dfs(len(s),"")
        return ans