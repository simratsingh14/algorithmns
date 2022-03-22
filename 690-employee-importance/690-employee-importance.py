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
        
        d = {}
        for emp in employees:
            d[emp.id] = [emp.importance,emp.subordinates]
        #print(d)
        
        def dfs(idx,d):
            importance = d[idx][0]
            for sub in d[idx][1]:
                importance+= dfs(sub,d)
            return importance
        return dfs(id,d)
            