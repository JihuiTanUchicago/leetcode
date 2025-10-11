from collections import defaultdict
class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        logs.sort(key=lambda x: x[0])
        group_number = defaultdict(int) # a person  -> a group
        new_group_num = 1
        groups = [] # list of set()
        for log in logs:
            timestamp, x, y = log
            if group_number[x] == 0 and group_number[y] == 0:
                group_number[x] = new_group_num
                group_number[y] = new_group_num
                new_set = set()
                new_set.add(x)
                new_set.add(y)
                groups.append(new_set)
                if len(groups[-1]) == n:
                    return timestamp
                new_group_num += 1
            elif group_number[x] != 0 and group_number[y] == 0:
                groups[group_number[x]-1].add(y)
                group_number[y] = group_number[x]
                if len(groups[group_number[y]-1]) == n:
                    return timestamp
            elif group_number[y] != 0 and group_number[x] == 0:
                groups[group_number[y]-1].add(x)
                group_number[x] = group_number[y]
                if len(groups[group_number[x]-1]) == n:
                    return timestamp
            elif group_number[x] != group_number[y]:
                a_set = groups[group_number[x]-1]
                a_set.update(groups[group_number[y]-1])
                groups[group_number[x]-1] = a_set
                for ele in groups[group_number[y]-1]:
                    group_number[ele] = group_number[x]
                if len(groups[group_number[x]-1]) == n:
                    return timestamp
        return -1


        