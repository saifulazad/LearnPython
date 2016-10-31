
def bread(fn):

    def wrap():
        print("/'''''''\\")
        fn()
        print('\________/')
    return wrap

def ingradiant(fn):
    def wrap():
        print('Tomato')
        print(fn())
        print('Salad')

    return wrap

@bread
@ingradiant
def food():
    return 'Food'



food()
