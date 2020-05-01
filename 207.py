from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        degrees=[0]*numCourses
        adjacency=[[] for i in range(numCourses)]
        queue=deque()
        for cur,pre in prerequisites:
            degrees[cur]+=1
            adjacency[pre].append(cur)
        for i in range(len(degrees)):
            if not degrees[i]:
                queue.append(i)
        while queue:
            pre=queue.popleft()
            numCourses-=1
            for cur in adjacency[pre]:
                degrees[cur]-=1
                if not degrees[cur]:
                    queue.append(cur)
        return not numCourses