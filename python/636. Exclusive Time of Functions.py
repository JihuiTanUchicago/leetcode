class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        log_stack = []
        output = [0 for i in range(n)]
        for log in logs:
            log = log.split(":")
            node_id, status, timestamp = log
            node_id = int(node_id)
            timestamp = int(timestamp)

            if status == "start":
                log_stack.append([node_id, timestamp])
            else:
                accumulated_time = 0 
                while type(log_stack[-1]) is int:
                    accumulated_time += log_stack.pop()
                node_id, start_timestamp = log_stack.pop()
                output[node_id] += timestamp - start_timestamp + 1 - accumulated_time
                if log_stack != []:
                    log_stack.append(timestamp - start_timestamp + 1)
            print(log_stack, output)
        
        return output