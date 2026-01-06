from collections import defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(set)
        post_graph = defaultdict(set)
        for prereq in prerequisites:
            a, b = prereq
            graph[a].add(b)
            post_graph[b].add(a)

        queue = []
        next_queue = []
        for course in range(numCourses):
            if len(graph[course]) == 0:
                queue.append(course)
        
        visited = set()
        while queue != []:
            course = queue.pop()
            visited.add(course)
            post_courses = list(post_graph[course])
            for post_course in post_courses:
                graph[post_course].remove(course)
                if len(graph[post_course]) == 0:
                    next_queue.append(post_course)
            
            if queue == []:
                queue = next_queue
                next_queue = []
        
        return len(visited) == numCourses
            

            
