class Cat:
    def ask_for_food(self):
        print(f'{self.name} хоче їсти')

fil = Cat()
fil.name = 'Филимон'
fil.age = 7
fil.fails = ['Впав в акваріум', 'Вкрав рибу']
fil.ask_for_food()

var = Cat()
var.name = 'Варежка'
var.ask_for_food()
