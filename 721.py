class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        emname={}
        graph=collections.defaultdict(set)
        for acc in accounts:
            name=acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                emname[email]=name
        seen=set()
        ans=[]
        for email in graph:
            if email not in seen:
                seen.add(email)
                stack=[email]
                component=[]
                while stack:
                    node=stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)   
                ans.append([emname[email]]+sorted(component))
        return ans              

