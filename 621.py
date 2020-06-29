class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count=[0]*26
        for ch in tasks:
            count[ord(ch)-ord('A')]+=1
        countmax=max(count)
        total=(countmax-1)*(n+1)
        for i in count:
            if i ==countmax:
                total+=1
        return max(total,len(tasks))