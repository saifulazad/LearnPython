

class Food(object):

    def __init__(self, name):
        self.name = name

    def test_food(self):
        raise NotImplementedError


class Pizza(Food):

    def __init__(self, name=None):
        super(Pizza, self).__init__(name=name or self.__class__.__name__)

    def test_food(self):
        print("{0} is good".format(self.name))

    def how_to_eat(self):
        raise NotImplementedError


class NormalPizza(Pizza):

    def __init__(self, name=None):
        super(NormalPizza, self).__init__(name=name or self.__class__.__name__)

    def test_food(self):
        print('{0} is tested Normal'.format(self.name))

    def how_to_eat(self):
        print('As it is {0} we will eat quickly'.format(self.name))


class HotPizza(Pizza):

    def __init__(self, name=None):
        super(HotPizza, self).__init__(name=name or self.__class__.__name__)

    def test_food(self):
        print('{0} is tested Hot'.format(self.name))

    def how_to_eat(self):
        print('As it is {0} we will eat slowly'.format(self.name))
if __name__ == '__main__':

    pizza = HotPizza('Pizza Hat er')

    pizza.test_food()
    pizza.how_to_eat()
