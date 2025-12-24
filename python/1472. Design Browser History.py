class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.current_index = 0

    def visit(self, url: str) -> None:
        self.current_index += 1
        if self.current_index >= len(self.history):
            self.history.append(url)
        else:
            self.history[self.current_index] = url
            self.history = self.history[:self.current_index+1]

    def back(self, steps: int) -> str:
        steps = min(self.current_index, steps)
        self.current_index -= steps
        return self.history[self.current_index]
        

    def forward(self, steps: int) -> str:
        steps = min(len(self.history)-1-self.current_index, steps)
        self.current_index += steps
        return self.history[self.current_index]


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)