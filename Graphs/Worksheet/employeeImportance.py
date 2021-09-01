from collections import deque

class Employee:
    def __init__(self, id: int, importance: int, subordinates):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates

class Solution:
    def getImportance(self, employees, id: int) -> int:
        
        employeeMap = {}
        for employee in employees:
            employeeMap[employee.id] = employee
            
        totalEmployeeValues = 0
        queue = deque()
        queue.append(id)
        
        while queue:
            currentId = queue.popleft()
            currentEmployee = employeeMap[currentId]
            totalEmployeeValues += currentEmployee.importance
            for subordinate in currentEmployee.subordinates:
                queue.append(subordinate)
        
        return totalEmployeeValues
