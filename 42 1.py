class Solution:
    def trap(self, height: List[int]) -> int:
        le=len(height)
        male=0
        mari=0
        an=[[0,0] for i in range(le)]
        for i in range(le):
            an[i][0]=male
            male=max(male,height[i])
        for i in range(le-1,-1,-1):
            an[i][1]=mari
            mari=max(mari,height[i])
        su=0
        for i in range(le):
            t=min(an[i][0],an[i][1])-height[i]
            if t>0:
                su+=t
        return su
            