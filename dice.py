import random

class Dice:
    """Represents a die with variable number of sides"""
    def __init__(self, sides):
        """Initiates die with 'sides' number of sides"""
        self.sides = sides
    def roll(self):
        """Rolls die and returns result
        Args: 
            sides(int): Number of sides
        Returns: An int which is the result from rolling die
        """
        return random.randint(0,sides)
        


if __name__ == __main__
    while True:
        """Keep making dice until code is stopped"""
        sides = input("Input the number of side of your die, or 'stop' to stop:")
        if sides.lower()!="stop":
            try:
                sides = int(sides)
                die = Dice(sides)
                reroll = "yes"
                """Allow user to roll die as many times as they wish"""
                while reroll.lower() == "yes" or reroll.lower() == "y":
                    print(str(die.roll()))
                    reroll = input("Reroll? ")
            except:
                print("Please input an integer or 'stop'.")
        else:
            break