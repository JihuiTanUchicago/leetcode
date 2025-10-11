class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        real_gas = []
        for i in range(len(gas)):
            real_gas.append(gas[i] - cost[i])
        start, end = 0,0
        total_gas = 0
        for i in range(len(gas)):
            if total_gas + real_gas[end] >= 0:
                total_gas += real_gas[end]
                end += 1
            else:
                if start == 0: 
                    start = len(gas)-1
                else:
                    start -= 1
                total_gas += real_gas[start]
        if total_gas >= 0:
            return start
        else:
            return -1

