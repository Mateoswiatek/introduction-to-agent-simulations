from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation


class RandomWalker(Agent):
    """An agent that walks randomly."""
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.x = self.random.randint(0, self.model.grid.width - 1)
        self.y = self.random.randint(0, self.model.grid.height - 1)
        self.model.grid.place_agent(self, (self.x, self.y))

    def step(self):
        """Move the agent to a random neighboring cell."""
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)

class PopulationModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            a = RandomWalker(i, self)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
