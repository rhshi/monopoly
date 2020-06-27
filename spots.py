class Spot(object):
    def __init__(self, name):
        self.name = name

    def board_setup(p, n):
        self.prev = p
        self.next = n

class Property(Spot):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color
        self.houses = 0
        self.hotels = 0

class Side(object):
    def __init__(self, spots, start, end):
        assert len(spot) != 0, "You gave no spots!"
        for i in range(1, len(spots)-1):
            spots[i].board_setup(spots[i-1], spots[i+1])
        
        spots[0].board_setup(start, sports[1])
        spots[-1].board_setup(spots[-2], end)

class Board(object):
    def __init__(self, 
        spots_N, 
        spots_S, 
        spots_E, 
        spots_W,
        nw,
        ne,
        sw,
        se 
    ):
        self.nw = nw
        self.ne = ne
        self.sw = sw
        self.se = se
        self.n = Side(spots_N, self.nw, self.ne)
        self.s = Side(spots_S, self.se, self.sw)
        self.e = Side(spots_E, self.sw, self.nw)
        self.w = Side(spots_W, self.ne, self.se)

