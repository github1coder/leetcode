class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        queue=collections.deque()
        degree=[0]*numCourses
        after=[[] for i in range(numCourses)]
        for i,j in prerequisites:
            degree[i]+=1
            after[j].append(i)
        for i in range(numCourses):
            if degree[i]==0:
                queue.append(i)
        su=0
        while queue:
            cur=queue.popleft()
            su+=1
            for i in after[cur]:
                degree[i]-=1
                if degree[i]==0:
                    queue.append(i)

        return su==numCourses 