from mesa import Agent, Model
from mesa.space import MultiGrid
from mesa.time import RandomActivation



class RandomWalker(Agent):
    """An agent that walks randomly."""
    def __init__(self, unique_id, model, group):
        super().__init__(unique_id, model)
        self.group = group
        self.x = self.random.randint(0, self.model.grid.width - 1)
        self.y = self.random.randint(0, self.model.grid.height - 1)
        self.model.grid.place_agent(self, (self.x, self.y))
        self.previous_position = (self.x, self.y)
        self.action_log = ""  # Dodatkowe pole do przechowywania informacji o działaniach agenta

    def step(self):
        """Move the agent to a random neighboring cell."""
        possible_steps = self.model.grid.get_neighborhood(
            self.pos,
            moore=True,
            include_center=False
        )
        self.previous_position = self.pos
        new_position = self.random.choice(possible_steps)
        self.model.grid.move_agent(self, new_position)
        self.action_log = f"Agent {self.unique_id} from group {self.group} moved from {self.previous_position} to {new_position}"


class PopulationModel(Model):
    """A model with some number of agents."""
    def __init__(self, N, width, height):
        self.num_agents = N
        self.grid = MultiGrid(width, height, True)
        self.schedule = RandomActivation(self)

        # Create agents
        for i in range(self.num_agents):
            group = 'A' if i < self.num_agents / 2 else 'B'
            a = RandomWalker(i, self, group)
            self.schedule.add(a)

    def step(self):
        """Advance the model by one step."""
        self.schedule.step()
