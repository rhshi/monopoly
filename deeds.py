class Deed(object):
    def __init__(self, mortgage, name):
        self.mortgage = mortgage
        self.name = name

    def rent():
        raise NotImplementedError

class Railroad(Deed):
    def __init__(self, mortgage, name):
        super().__init__(mortgage, name)

    def rent(self, num_rr):
        if num_rr == 1:
            return 25
        elif num_rr == 2:
            return 50
        elif num_rr == 3:
            return 100
        elif num_rr == 4:
            return 200
        else:
             raise ValueError("You cannot own that many railroads!")

class Utility(Deed):
    def __init__(self, mortgage, name):
        super().__init__(mortgage, name)

    def rent(self, dice, num_u):
        if num_u == 1:
            return 4 * dice
        elif num_u == 2:
            return 10 * dice
        else:
            raise ValueError("You cannot own that many utilities!")

class Property(Deed):
    def __init__(self, 
        mortgage, 
        name,
        color,
        base_rent, 
        house_1, 
        house_2,
        house_3,
        house_4,
        hotel,
        house_cost,
        hotel_cost
    ):
        super().__init__(mortgage, name)
        self.color = color
        self.base_rent = base_rent
        self.house_1 = house_1
        self.house_2 = house_2
        self.house_3 = house_3
        self.house_4 = house_4
        self.hotel = hotel
        self.house_cost = house_cost
        self.hotel_cost = hotel_cost

    def rent(self, hotel, houses, all_own):
        if hotel:
            return self.hotel
        elif houses == 1:
            return self.house_1
        elif houses == 2:
            return self.house_2
        elif houses == 3:
            return self.house_3
        elif houses == 4:
            return self.house_4
        elif all_own:
            return 2 * self.base_rent
        else:
            return self.base_rent