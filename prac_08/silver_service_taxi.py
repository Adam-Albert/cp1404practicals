"""
CP1404/CP5632 Practical
silver service .
"""
from taxi import Taxi


class SilverServiceTaxi(Taxi):
    """A variation of car"""
    flagfall = 4.5

    def __init__(self, name, fuel, fanciness):
        """Initialise a unreliable car instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.fanciness = fanciness
        self.price_per_km *= fanciness

    def get_fare(self):
        """Return the price for the taxi trip."""
        return self.flagfall + super().get_fare()

    def __str__(self):
        """return a sting of a SilverServiceTaxi."""
        return "{} plus flagfall of ${:.2f}".format(super().__str__(), self.flagfall)





