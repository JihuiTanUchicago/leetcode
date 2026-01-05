class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        graph = {}
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            domain_ls = domain.split(".")
            cur = graph
            for i in range(len(domain_ls)-1, -1, -1):
                if domain_ls[i] not in cur:
                    cur[domain_ls[i]] = {}
                cur = cur[domain_ls[i]]
                if i == 0:
                    if "/END/" not in cur:
                        cur["/END/"] = count
                    else:
                        cur["/END/"] += count
        
        output = []
        def dfs(cur, name):
            count = 0
            for child in cur:
                if child == "/END/":
                    count += cur["/END/"]
                else:
                    count += dfs(cur[child], child+"."+name)
            output.append(f"{count} {name}")
            return count

        for child in graph:
            dfs(graph[child], child)
        
        return output
                    
                
            