from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        ''' this is a cycle detection problem. when we detect a cycle, we say false
        what will be the "true" then? 
        im assuming that if the length of visited set is equal to numCourses, we can say true'''

        graph = defaultdict(list)
        indegree = [0] * numCourses
        taken = 0

        for dp, pr in prerequisites:
            graph[pr].append(dp)
            indegree[dp] += 1
        
        q = deque([n for n in range(numCourses) if indegree[n] == 0])

        while q:
            course = q.popleft()
            taken += 1

            for x in graph[course]:
                indegree[x] -= 1

                if indegree[x] == 0:
                    q.append(x)
        return taken == numCourses



        

        

        


        
        