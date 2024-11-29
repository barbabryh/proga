
#Стратегия
from abc import ABC, abstractmethod

class Strategy(ABC):
    @abstractmethod
    def do_operation(self, num1: int, num2: int) -> int:
        pass

class OperationAdd(Strategy):
    def do_operation(self, num1: int, num2: int) -> int:
        return num1 + num2

class OperationSubtract(Strategy):
    def do_operation(self, num1: int, num2: int) -> int:
        return num1 - num2

class OperationMultiply(Strategy):
    def do_operation(self, num1: int, num2: int) -> int:
        return num1 * num2

class Context:
    def __init__(self, strategy: Strategy):
        self._strategy = strategy

    def execute_strategy(self, num1: int, num2: int) -> int:
        return self._strategy.do_operation(num1, num2)

context = Context(OperationAdd())
print("10 + 5 =", context.execute_strategy(10, 5))

context = Context(OperationSubtract())
print("10 - 5 =", context.execute_strategy(10, 5))

context = Context(OperationMultiply())
print("10 * 5 =", context.execute_strategy(10, 5))


#Цепочка обязанностей
from abc import ABC, abstractmethod

class Handler(ABC):
    def __init__(self, successor=None):
        self._successor = successor

    @abstractmethod
    def handle(self, request):
        pass

class ConcreteHandler1(Handler):
    def handle(self, request):
        if request == "one":
            print("ConcreteHandler1 handled the request")
        elif self._successor is not None:
            self._successor.handle(request)

class ConcreteHandler2(Handler):
    def handle(self, request):
        if request == "two":
            print("ConcreteHandler2 handled the request")
        elif self._successor is not None:
            self._successor.handle(request)

class ConcreteHandler3(Handler):
    def handle(self, request):
        if request == "three":
            print("ConcreteHandler3 handled the request")
        elif self._successor is not None:
            self._successor.handle(request)

handler1 = ConcreteHandler1()
handler2 = ConcreteHandler2(handler1)
handler3 = ConcreteHandler3(handler2)

handler3.handle("two")  
handler3.handle("three")  
handler3.handle("one")  


#Итератор
class Iterator:
    def __init__(self, collection):
        self._collection = collection
        self._index = 0

    def __next__(self):
        try:
            value = self._collection[self._index]
            self._index += 1
            return value
        except IndexError:
            raise StopIteration

    def __iter__(self):
        return self

class Collection:
    def __init__(self):
        self._items = []

    def add_item(self, item):
        self._items.append(item)

    def __iter__(self):
        return Iterator(self._items)

collection = Collection()
collection.add_item("item1")
collection.add_item("item2")
collection.add_item("item3")

for item in collection:
    print(item)  # Вывод: item1, item2, item3
