#singleton
class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            cls._instance = super(Singleton, cls).__new__(cls)
            # Инициализация, если необходимо
        return cls._instance

    def some_method(self):
        # Реализация метода
        pass

# Пример использования
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)

#Factory method
from abc import ABC, abstractmethod

# Интерфейс для продукта (логгера)
class Logger(ABC):
    @abstractmethod
    def log(self, message: str):
        pass

# Конкретный продукт: Файловый логгер
class FileLogger(Logger):
    def log(self, message: str):
        print(f"Logging to file: {message}")

# Конкретный продукт: Консольный логгер
class ConsoleLogger(Logger):
    def log(self, message: str):
        print(f"Logging to console: {message}")

# Создатель (фабрика)
class LoggerFactory(ABC):
    @abstractmethod
    def create_logger(self) -> Logger:
        pass

    # Метод, использующий фабричный метод
    def log_message(self, message: str):
        logger = self.create_logger()
        logger.log(message)

# Конкретный создатель: Фабрика для файлового логгера
class FileLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return FileLogger()

# Конкретный создатель: Фабрика для консольного логгера
class ConsoleLoggerFactory(LoggerFactory):
    def create_logger(self) -> Logger:
        return ConsoleLogger()

# Пример использования
if __name__ == "__main__":
    file_logger_factory = FileLoggerFactory()
    file_logger_factory.log_message("This is a file log message.")

    console_logger_factory = ConsoleLoggerFactory()
    console_logger_factory.log_message("This is a console log message.")

#abstract factory
from abc import ABC, abstractmethod

# Интерфейс для продукта A
class Button(ABC):
    @abstractmethod
    def paint(self):
        pass

# Конкретный продукт A1
class WindowsButton(Button):
    def paint(self):
        print("You have created a Windows button.")

# Конкретный продукт A2
class MacButton(Button):
    def paint(self):
        print("You have created a Mac button.")

# Интерфейс для продукта B
class Checkbox(ABC):
    @abstractmethod
    def paint(self):
        pass

# Конкретный продукт B1
class WindowsCheckbox(Checkbox):
    def paint(self):
        print("You have created a Windows checkbox.")

# Конкретный продукт B2
class MacCheckbox(Checkbox):
    def paint(self):
        print("You have created a Mac checkbox.")

# Интерфейс абстрактной фабрики
class GUIFactory(ABC):
    @abstractmethod
    def create_button(self) -> Button:
        pass

    @abstractmethod
    def create_checkbox(self) -> Checkbox:
        pass

# Конкретная фабрика 1
class WindowsFactory(GUIFactory):
    def create_button(self) -> Button:
        return WindowsButton()

    def create_checkbox(self) -> Checkbox:
        return WindowsCheckbox()

# Конкретная фабрика 2
class MacFactory(GUIFactory):
    def create_button(self) -> Button:
        return MacButton()

    def create_checkbox(self) -> Checkbox:
        return MacCheckbox()

# Клиентский код
class Application:
    def __init__(self, factory: GUIFactory):
        self.button = factory.create_button()
        self.checkbox = factory.create_checkbox()

    def paint(self):
        self.button.paint()
        self.checkbox.paint()

# Пример использования
if __name__ == "__main__":
    app1 = Application(WindowsFactory())
    app1.paint()

    app2 = Application(MacFactory())
    app2.paint()


#Builder
# Продукт
class Pizza:
    def __init__(self):
        self.dough = None
        self.sauce = None
        self.topping = None

    def set_dough(self, dough):
        self.dough = dough

    def set_sauce(self, sauce):
        self.sauce = sauce

    def set_topping(self, topping):
        self.topping = topping

    def __str__(self):
        return f"Pizza(dough='{self.dough}', sauce='{self.sauce}', topping='{self.topping}')"


# Интерфейс строителя
class PizzaBuilder:
    def build_dough(self):
        pass

    def build_sauce(self):
        pass

    def build_topping(self):
        pass

    def get_result(self):
        pass


# Конкретный строитель
class HawaiianPizzaBuilder(PizzaBuilder):
    def __init__(self):
        self.pizza = Pizza()

    def build_dough(self):
        self.pizza.set_dough("cross")

    def build_sauce(self):
        self.pizza.set_sauce("mild")

    def build_topping(self):
        self.pizza.set_topping("ham+pineapple")

    def get_result(self):
        return self.pizza


# Директор
class PizzaDirector:
    def __init__(self, builder: PizzaBuilder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.build_dough()
        self.builder.build_sauce()
        self.builder.build_topping()


# Пример использования
if __name__ == "__main__":
    builder = HawaiianPizzaBuilder()
    director = PizzaDirector(builder)

    director.construct_pizza()
    pizza = builder.get_result()

    print(pizza)

