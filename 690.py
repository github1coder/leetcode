"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        self.s=0
        dic={}
        j=0
        for i in employees:
            dic[i.id]=j
            j+=1
        def bfs(id):
            self.s+=employees[id].importance
            if employees[id].subordinates==[]:
                return
            for i in employees[id].subordinates:
                bfs(dic[i])
        bfs(dic[id])
        return self.s