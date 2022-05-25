class Cat:
    def __init__(self, name):
        self.name = name
    def ask_for_food(self):
        print('Cat {} wants to eat'.format(self.name))

class Dog:
    def __init__(self, name):
        self.name = name
    def ask_for_food(self):
        print('Dog {} wants to eat'.format(self.name))

class Raccoon:
    def __init__(self, name):
        self.name = name
    def ask_for_food(self):
        print('Raccoon {} wants to eat'.format(self.name))

murzik = Cat('Murzik')
rex = Dog('Rex')
rac = Raccoon('Rac')

murzik.ask_for_food()
rex.ask_for_food()
rac.ask_for_food()
