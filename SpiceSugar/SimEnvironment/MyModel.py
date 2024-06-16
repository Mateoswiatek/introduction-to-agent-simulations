from mesa import Model

from SpiceSugar.SimEnvironment.agent.Spice import Spice
from SpiceSugar.SimEnvironment.agent.Sugar import Sugar
from SpiceSugar.SimEnvironment.agent.Trader import Trader


class MyModel(Model):
    """
    A model class to manage Sugarspace with Traders
    """
    def __init__(self):
        super().__init__()
        print("Its a model")
        self.sugar = Sugar()
        self.spice = Spice()
        self.trader = Trader()
