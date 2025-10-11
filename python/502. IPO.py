class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        projects = sorted(list(zip(profits, capital)), key=lambda x: (-x[0], x[1]))
        print(projects)
        while k != 0:
            index = -1
            for i in range(len(projects)):
                profit, capital = projects[i]
                if w >= capital:
                    w += profit
                    index = i
                    break
            if index >= 0:
                projects.pop(index)
            else:
                break
            k -= 1
        return w



            