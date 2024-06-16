from mesa import Agent


class Trader(Agent):
    """
    Trader agent:
    - has a metabolism for sugar and spice
    - harvest and traders sugar and spice to survive and thrive
    """

    def __init__(self):
        print("I'm a Trader")
