def get_valid_input(input_string, valid_options):
    """
    function to check whether input mathes one of the options
    :param input_string: input
    :param valid_options: tuple of valid options
    """
    input_string += "({})".format(", ".join(valid_options))
    response = input(input_string)
    while response.lower() not in valid_options:
        response = input(input_string)
    return response


class Property:
    """
    Represent agent's property
    """
    def __init__(self, square_feet=" ", beds=" ",
                 baths="", **kwargs):
        """
        Initialize property with square footage, number of beds and baths
        """
        super().__init__(**kwargs)
        self.square_feet = square_feet
        self.num_bedrooms = beds
        self.num_baths = baths

    def display(self):
        """
        Display information about the property
        """
        print("PROPERTY DETAILS")
        print("----------------")
        print("Square footage: {}".format(self.square_feet))
        print("bedrooms: {}".format(self.num_bedrooms))
        print("bathrooms: {}".format(self.num_baths), "\n")

    def prompt_init():
        """
        Input function for parameters
        """
        return dict(square_feet=input("Enter the square feet:"),
                    beds=input("Enter number of bedrooms: "),
                    baths=input("Enter number of baths: "))
    prompt_init = staticmethod(prompt_init)


class Apartment(Property):
    """
    Represents apartment class inherited from property
    """
    valid_laundries = ("coin", "ensuite", "none")
    valid_balconies = ("yes", "no", "solarium")

    def __init__(self, balcony='', laundry='', **kwargs):
        """
        Initialize apartments with type of balcony and laundry
        """
        super().__init__(**kwargs)
        self.balcony = balcony
        self.laundry = laundry

    def display(self):
        """
        Display information about apartment
        """
        super().display()
        print("APARTMENT DETAILS")
        print("laundry: {}".format(self.laundry))
        print("has balcony: {}".format(self.balcony))

    def prompt_init():
        """
        Input function for apartment's parameters
        """
        parent_init = Property.prompt_init()
        laundry = get_valid_input("What laundry facilities does "
                                  "the property have?",
                                  Apartment.valid_laundries)
        balcony = get_valid_input("Does the property have a balcony?",
                                  Apartment.valid_balconies)
        parent_init.update({"laundry": laundry, "balcony": balcony})

        return parent_init
    prompt_init = staticmethod(prompt_init)


class House(Property):
    """
    Represents house class inherited from property
    """
    valid_garage = ("attached", "detached", "none")
    valid_fenced = ("yes", "no")

    def __init__(self, num_stories='', garage='', fenced='', **kwargs):
        """
        Initialize house with number of stories, garage and fence types
        """
        super().__init__(**kwargs)
        self.garage = garage
        self.fenced = fenced
        self.num_stories = num_stories

    def display(self):
        """
        Display information about the house
        """
        super().display()
        print("HOUSE DETAILS")
        print("# of stories: {}".format(self.num_stories))
        print("garage: {}".format(self.garage))
        print("fenced yard: {}".format(self.fenced))

    def prompt_init():
        """
        Input function for house' parameters
        """
        parent_init = Property.prompt_init()
        fenced = get_valid_input("Is the yard fenced? ",
                                 House.valid_fenced)
        garage = get_valid_input("Is there a garage? ",
                                 House.valid_garage)
        num_stories = input("How many stories? ")

        parent_init.update({
            "fenced": fenced,
            "garage": garage,
            "num_stories": num_stories
        })
        return parent_init
    prompt_init = staticmethod(prompt_init)

