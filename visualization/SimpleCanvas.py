from mesa.visualization.ModularVisualization import VisualizationElement
import math


class SimpleCanvas(VisualizationElement):
    local_includes = ["visualization/simple_continuous_canvas.js", "visualization/test.js", "visualization/test.js"]

    def __init__(self, portrayal_method, canvas_height=500, canvas_width=500):
        """
        Instantiate a new SimpleCanvas
        """
        self.portrayal_method = portrayal_method
        self.canvas_height = canvas_height
        self.canvas_width = canvas_width
        new_element = f"new Simple_Continuous_Module({self.canvas_width}, {self.canvas_height})"
        self.js_code = "elements.push(" + new_element + ");"

    def render(self, model):
        space_state = []
        for obj in model.schedule.agents:
            portrayal = self.portrayal_method(obj)
            x, y = obj.pos
            x = (x - model.grid.x_min) / (model.grid.x_max - model.grid.x_min)
            y = (y - model.grid.y_min) / (model.grid.y_max - model.grid.y_min)
            portrayal["x"] = x
            portrayal["y"] = y
            space_state.append(portrayal)
        return space_state

    # def render_agent(self, agent):
    #     portrayal = self.portrayal_method(agent)
    #     return portrayal
    #
    # def render(self, model):
    #     space_state = []
    #     agent_portrayals = [self.render_agent(agent) for agent in model.schedule.agents]
    #
    #     space_state.append(agent_portrayals)
    #     return space_state

    def __call__(self, model):
        return self.render(model)
