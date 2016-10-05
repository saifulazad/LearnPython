
from factorypattern import (
                                NormalPizza,
                                HotPizza,
                            )


def create_pizza(pizza_type=None):
    """

    pizza creator function. here we just
    pass pizza name as str and return
    that pizza


    :param pizza_type:
    :return: pizza class
    :raise KeyError, if one can not find pizza
    by calling specific name

    """
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
