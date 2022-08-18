# у класса кэмэлкейс
class MyAuto:
    """my auto class"""
    # атрибуты класса
    a_count = 0

    # конструктор
    # атрибуты объекта
    def __init__(self, n, m, y):
        self.name = n
        self.model = m
        self.year = y
        MyAuto.a_count += 1

    # методы класса
    def on_start(self):
        print(f'Go - go! {self.name}')
        self.on_stop()

    def on_stop(self):
        print('Stop.')


auto_1 = MyAuto('Lada', 'Vesta', 2017)
print(auto_1.a_count)
auto_2 = MyAuto('Audo', 'A5', 2022)
print(auto_2.a_count)
