class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        le=len(arr)
        an=[0]*le
        queue=collections.deque([start])
        an[start]=1
        while queue:
            t=queue.popleft()
            if arr[t]==0:
                return True
            if t+arr[t]<le and an[t+arr[t]]==0:
                queue.append(t+arr[t])
                an[t+arr[t]]=1
            if t-arr[t]>=0 and an[t-arr[t]]==0:
                queue.append(t-arr[t])
                an[t-arr[t]]=1
        return False