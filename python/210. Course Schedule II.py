from collections import defaultdict

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        postreq = defaultdict(set)
        prereq = defaultdict(set)
        for courses in prerequisites:
            a, b = courses
            prereq[a].add(b)
            postreq[b].add(a)
        courses = []
        current_queue = []
        next_queue = []
        for i in range(numCourses):
            if i not in prereq:
                current_queue.append(i)
                courses.append(i)
        while current_queue != []:
            course = current_queue.pop()
            for post_course in postreq[course]:
                prereq[post_course].remove(course)
                if prereq[post_course] == set():
                    next_queue.append(post_course)
                    courses.append(post_course)
            
            if current_queue == []:
                current_queue = next_queue
                next_queue = []
        if len(courses) == numCourses:
            return courses
        return []


            
        
