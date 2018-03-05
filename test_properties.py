import buildings
import actions


def test_property():
    print(buildings.Property(23, 2, 2).square_feet)
    buildings.Property(23, 2, 2).display()
    buildings.Property().prompt_init()


def test_house():
    print(buildings.House(23, 2, 2).square_feet)
    buildings.House().display()
    buildings.House().prompt_init()


def test_apartment():
    print(buildings.Apartment().square_feet)
    buildings.Apartment().display()
    buildings.Apartment().prompt_init()



test_apartment()
