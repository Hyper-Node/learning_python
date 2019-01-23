# create second class which can store functions in a category ( like normalize)


class Normalize(object):
    def __init__(self, base):
        self.base = base

    def calc_currency(self):
        return self.base.test_property


class Base(object):
    def __init__(self):
        self.test_property = 1
        self.normalize = Normalize(self)





b = Base()
val = b.normalize.calc_currency()
print(val)