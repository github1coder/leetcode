class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        le=len(cost)
        for i in range(2,le):
            cost[i]+=min(cost[i-1],cost[i-2])
        return min(cost[le-1],cost[le-2])