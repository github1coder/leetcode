class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degree=[0]*numCourses
        dic=[[] for i in range(numCourses)]
        n=numCourses
        an=[]
        for cur,pre in prerequisites:
            degree[cur]+=1
            dic[pre].append(cur)
        for i in range(numCourses):
            if degree[i]==0:
                an.append(i)
        while an:
            n-=1
            pre=an.pop()
            for i in dic[pre]:
                degree[i]-=1
                if degree[i]==0:
                    an.append(i)
        return n==0