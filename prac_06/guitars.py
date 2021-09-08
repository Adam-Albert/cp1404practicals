
VINTAGE_AGE = 50


class Guitars:

    def __init__(self, name="", cost=0, year=0):
        self.cost = cost
        self.name = name
        self.year = year

    def __str__(self):
        return "{} ({}) : {:.2}".format(self.name, self.year, self.cost)

    def get_age(self):
        return 2021 - self.year

    def is_vintage(self):
        return self.get_age() >= VINTAGE_AGE
