from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        degree=[0]*numCourses
        later=[[] for i in range(numCourses)]
        num=[]
        queue=deque()
        for cur, pre in prerequisites:
            degree[cur]+=1
            later[pre].append(cur)
        for i in range(numCourses):
            if degree[i]==0:
                queue.append(i)
        while queue:
            pre=queue.popleft()
            num.append(pre)
            numCourses-=1
            for i in later[pre]:
                degree[i]-=1
                if degree[i]==0:
                    queue.append(i)
        if numCourses==0:
            return num
        return []