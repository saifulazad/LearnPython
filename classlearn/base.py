
class Base(object):

    def __init__(self):
        pass

    def print_derived_class_param(self):
        print(self.derived_vlaue)


class Derived(Base):

    def __init__(self, x):
        super(Derived, self).__init__()
        self.derived_vlaue = x


if __name__ == '__main__':

    derived = Derived(12)

    derived.print_derived_class_param()
