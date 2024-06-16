from mesa import Agent


class Spice(Agent):
    """
    Spice:
    - contains an amount of spice
    - grows 1 amount of spice at each turn
    """

    def __init__(self):
        print("I'm a Spice agent")
