from mesa import Agent


class Sugar(Agent):
    """
    Sugar agent:
    - contains an amount of sugar
    - grows 1 amount of sugar at each turn
    """

    def __init__(self):
        print("I'm a Sugar agent")
