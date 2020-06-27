import glob
import deeds as d
import spots as s


def setup():
    cards = {}

    for filepath in glob.iglob("deeds/*.txt"):
        with open(filepath, "r") as f:
            lines = list(map(lambda x: x.strip(), f.readlines()))
            if lines[0] == "title deed":
                card = d.Property(
                    mortgage=int(lines[9]),
                    name=lines[1],
                    color=lines[2],
                    base_rent=int(lines[3]), 
                    house_1=int(lines[4]), 
                    house_2=int(lines[5]),
                    house_3=int(lines[6]),
                    house_4=int(lines[7]),
                    hotel=int(lines[8]),
                    house_cost=int(lines[10]),
                    hotel_cost=int(lines[11])
                )
            elif lines[0] == "utility":
                card = d.Utility(
                    mortgage=int(lines[2]),
                    name=lines[1]
                )
            elif lines[0] == "railroad":
                card = d.Railroad(
                    mortgage=int(lines[6]),
                    name=lines[1]
                )
            else:
                raise ValueError("You have a mysterious deed card!")
            cards[lines[1]] = card
        
    print(cards)


def main():
    setup()

if __name__ == "__main__":
    main()