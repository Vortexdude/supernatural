
class NewDecorator:
    def __init__(self, n):
        self.n = n

    def __call__(self, fun):
        def wrapper(*args, **kwargs):
            print("from class Decorator")
            print(self.n*"*")
            fun(*args, **kwargs)
            print("from class Decorator")

        return wrapper

@NewDecorator
def add(a, b):
    return a + b


add(2,3)


class Resource:
    def get(self):
        return {"Status": "200"}

