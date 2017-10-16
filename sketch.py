class Deck:
    def  __init__(self):
        self.cards_dict = {}
        self.deck = [x for x in range(50)]
        self.manual_take = True
        self.players = [1, 2, 3, 4]
        self.players_nicks = {1:"Gra4" }
        self.dict_functions = {}

    def next(self, stack):
        """Двигает стак вправо по кругу"""
        stack.append(stack[0])
        del stack[0]
        return stack

    def switch_manual_take(self):
        """Меняет bool на противоположное значение"""
        if self.manual_take == True:
            self.manual_take = False
        else:
            self.manual_take = True

        return self.manual_take


    def add_func_in_dict(func):
        """Добавляет функцию в словарь,
        вырезая из имени цифры"""
         number = ''
         for i in func.__name__:
             if i.isdigit():
                 number += i
         self.dict_functions[int(number)] = func
         def wrapper(*args):
             func(*args)
             return func
         return wrapper

