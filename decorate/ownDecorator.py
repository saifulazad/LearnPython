


def makebolt(fn):
    def new_func():
        return '<b>' + fn() + '</b>'
    return new_func

@makebolt
def hello():
    return 'Hello'




print(hello())





