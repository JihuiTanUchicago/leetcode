class Logger:

    def __init__(self):
        self.message_time_hash = {}

        

    def shouldPrintMessage(self, timestamp: int, message: str) -> bool:
        prev_time = self.message_time_hash.get(message, None)
        if prev_time == None or prev_time <= timestamp - 10:
            self.message_time_hash[message] = timestamp
            return True
        return False
        


# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)