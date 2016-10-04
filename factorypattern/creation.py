
from factorypattern import (
                                NormalPizza,
                                HotPizza,
                            )


def create_pizza(pizza_type=None):

    pizzas = {'NormalPizza': NormalPizza, 'HotPizza': HotPizza}

    try:
        return pizzas[pizza_type]

    except KeyError:
        raise KeyError

if __name__ == '__main__':

    My_pizza = create_pizza('NormalPizza')

    my_pizza_with_shop = My_pizza('KFC')

    my_pizza_with_shop.test_food()
    my_pizza_with_shop.how_to_eat()
