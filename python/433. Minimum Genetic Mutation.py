class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        visited = {b:False for b in bank}
        global_count = float('inf')
        startGene = startGene
        endGene = endGene

        def explore(count):
            nonlocal startGene, global_count

            if count >= global_count:
                return

            if startGene == endGene:
                global_count = min(global_count, count)
                return

            for i in range(len(startGene)):
                for c in "ACGT":
                    if c == startGene[i]:
                        continue
                    mutation_after_change= startGene[:i] + c + startGene[i+1:]
                    if mutation_after_change in visited.keys() and visited[mutation_after_change] == False:
                        temp = startGene
                        startGene = mutation_after_change
                        visited[mutation_after_change] = True
                        explore(count+1)
                        visited[mutation_after_change] = False
                        startGene = temp

        if startGene == endGene:
            return 0
        explore(0)
        return -1 if global_count == float('inf') else global_count

                

