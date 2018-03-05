from buildings import Property, House, Apartment, get_valid_input


class Purchase:
    """
    Represents class for purchasing property
    """
    def __init__(self, price='', taxes='', **kwargs):
        """
        Initialize property with price and taxes
        """
        super().__init__(**kwargs)
        self.price = price
        self.taxes = taxes

    def display(self):
        """
        Display information about the purchase
        """
        super().display()
        print("PURCHASE DETAILS")
        print("selling price: {}".format(self.price))
        print("estimated taxes: {}".format(self.taxes))

    def prompt_init():
        """
        Input function for purchasing parameters
        """
        return dict(price=input('selling price: '),
                    taxes=input("estimated taxes: "))
    prompt_init = staticmethod(prompt_init)


class Rental:
    """
    Represents class for rental property
    """
    def __init__(self, furnished='', utilities='', rent='', **kwargs):
        super().__init__(**kwargs)
        self.furnished = furnished
        self.rent = rent
        self.utilities = utilities

    def display(self):
        """
        Display information about the rent
        """
        super().display()
        print("RENTAL DETAILS")
        print("rent: {}".format(self.rent))
        print("estimated utilities: {}".format(self.utilities))
        print("furnished: {}".format(self.furnished))

    def prompt_init():
        """
        Input function for renting parameters
        """
        return dict(
            rent=input("What is the monthly rent? "),
            utilities=input("What are estimated utilities? "),
            furnished=get_valid_input("Is the property furnished?",
                                      ("yes", "no")))
    prompt_init = staticmethod(prompt_init)


class HouseRental(Rental, House):
    def prompt_init():
        """
        Input function for house renting parameters
        """
        init = House.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentRental(Rental, Apartment):
    """
    Input function for apartment renting parameters
    """
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Rental.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class HousePurchase(Purchase, House):
    """
    Input function for house purchasing parameters
    """
    def prompt_init():
        init = House.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class ApartmentPurchase(Purchase, Apartment):
    """
    Input function for apartment purchasing parameters
    """
    def prompt_init():
        init = Apartment.prompt_init()
        init.update(Purchase.prompt_init())
        return init
    prompt_init = staticmethod(prompt_init)


class Agent:
    """
    Represents agent purchasing or renting property
    """
    type_map = {
        ("house", "rental"): HouseRental,
        ("house", "purchase"): HousePurchase,
        ("apartment", "rental"): ApartmentRental,
        ("apartment", "purchase"): ApartmentPurchase
    }

    def __init__(self):
        """
        Initialize agent with empty property list
        """
        self.property_list = []

    def display_properties(self):
        """
        Display all properties
        """
        for property in self.property_list:
            property.display()

    def add_property(self):
        """
        Adds new property to the property list
        """
        property_type = get_valid_input(
            "What type of property? ",
            ("house", "apartment")).lower()
        payment_type = get_valid_input(
            "What payment type? ",
            ("purchase", "rental")).lower()

    def find_property(self, key_name, value):
        """
        Finds property with given key parameter
        """
        for pr in self.property_list:
            if pr.key_name == value:
                return property
        else:
            return None

    def delete_property(self, property_index):
        """
        Delete property from the property list by its index
        """
        del self.property_list[property_index]

        PropertyClass = self.type_map[(property_type, payment_type)]
        init_args = PropertyClass.prompt_init()
        self.property_list.append(PropertyClass(**init_args))
