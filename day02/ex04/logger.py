import time
from random import randint
import getpass


def log(func):
    def wrapper(*args, **kwargs):
        funcName = ''
        if func.__name__ == 'start_machine':
            funcName = 'Start Machine\t\t'
        elif func.__name__ == 'boil_water':
            funcName = 'Boil Water\t\t'
        elif func.__name__ == 'make_coffee':
            funcName = 'Make Coffee\t\t'
        elif func.__name__ == 'add_water':
            funcName = 'Add Water\t\t\t'
        userName = '({})Running:'.format(getpass.getuser())
        s = time.time()
        result = func(*args, **kwargs)
        e = time.time()
        unit = "ms"
        if e - s >= 1:
            unit = "s "
        open('machine.log', 'a+').write("{} {} [ exec-time =  {:.3f} {} ]\n".format(userName, funcName, e - s, unit))
        return result
    return wrapper


class CoffeeMachine():
    water_level = 100
   
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False

    @log
    def boil_water(self):
        return "boiling..."

    @log
    def make_coffee(self):
        if self.start_machine():
            for _ in range(20):
                time.sleep(0.1)
                self.water_level -= 1
            print(self.boil_water())
            print("Coffee is ready!")

    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))
        self.water_level += water_level
        print("Blub blub blub...")


if __name__ == "__main__":
    machine = CoffeeMachine()
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    machine.add_water(70)