import threading

class Foo:
    def __init__(self):
        self.condition1 = threading.Condition()
        self.condition2 = threading.Condition()


    def first(self, printFirst: 'Callable[[], None]') -> None:
        
        # printFirst() outputs "first". Do not change or remove this line.
        printFirst()
        with self.condition1:
            self.condition1.notify()


    def second(self, printSecond: 'Callable[[], None]') -> None:
        
        # printSecond() outputs "second". Do not change or remove this line.
        with self.condition1:
            self.condition1.wait()
        printSecond()
        with self.condition2:
            self.condition2.notify()


    def third(self, printThird: 'Callable[[], None]') -> None:
        
        # printThird() outputs "third". Do not change or remove this line.
        with self.condition2:
            self.condition2.wait()
        printThird()