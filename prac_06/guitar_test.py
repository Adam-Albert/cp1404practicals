
from guitar import Guitar


def test_guitar():
    """test the guitar class"""
    gibson = Guitar("gibson", 16000.400, 1971)
    print(gibson)
    print("expected 50 got", gibson.get_age())
    print("expected true got", gibson.is_vintage())

    another_guitar = Guitar("another guitar", 2000.0000, 1999)
    print(another_guitar)
    print("expected 22 got", another_guitar.get_age())
    print("expected False got", another_guitar.is_vintage())


test_guitar()
