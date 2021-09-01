class Solution:
    def findOrder(self, numCourses: int, prerequisites):
        validOrder = []
        if not prerequisites:
            return [i for i in range(numCourses)]
        
        inDegree = {i:0 for i in range(numCourses)}
        
        for i in range(0, len(prerequisites)):
            inDegree[prerequisites[i][0]] += 1
        
        topologicalStack = []
        for i in range(len(inDegree)):
            if inDegree[i] == 0:
                topologicalStack.append(i)
        
        while topologicalStack:
            
            current = topologicalStack.pop()
            validOrder.append(current)
            for i in range(0, len(prerequisites)):
                if prerequisites[i][1] == current:
                    inDegree[prerequisites[i][0]] -= 1
                    if(inDegree[prerequisites[i][0]] == 0):
                        topologicalStack.append(prerequisites[i][0])
        
        if len(validOrder) != numCourses:
            return []
        return validOrder

if __name__ == '__main__':
    sol = Solution()
    print(sol.findOrder(2, [[1,0]]))
    print(sol.findOrder(4, [[1,0], [2,0], [3,1], [3,2]]))