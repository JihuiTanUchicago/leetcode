class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        province_count = 0
        visited_cities = [False for i in range(len(isConnected))]
        stack = [0]
        visited_cities[0] = True
        while stack != []:
            city_i = stack.pop()
            for c in range(len(isConnected)):
                if isConnected[city_i][c] == 1 and visited_cities[c] == False:
                    stack.append(c)
                    visited_cities[c] = True
            if stack == []:
                province_count += 1
                for i in range(len(visited_cities)):
                    if visited_cities[i] == False:
                        stack.append(i)
                        visited_cities[i] = True
                        break
        
        return province_count
