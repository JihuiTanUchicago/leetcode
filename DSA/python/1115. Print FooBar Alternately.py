import threading

class FooBar:
    def __init__(self, n):
        self.n = n
        self.condition = threading.Condition()
        self.foo_turn = True


    def foo(self, printFoo: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                # printFoo() outputs "foo". Do not change or remove this line.
                while self.foo_turn == False:
                    self.condition.wait()
                printFoo()
                self.foo_turn = False
                self.condition.notify()


    def bar(self, printBar: 'Callable[[], None]') -> None:
        for i in range(self.n):
            with self.condition:
                # printBar() outputs "bar". Do not change or remove this line.
                while self.foo_turn == True:
                    self.condition.wait()
                printBar()
                self.foo_turn = True
                self.condition.notify()