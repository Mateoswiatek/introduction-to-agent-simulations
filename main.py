from MyModel import PopulationModel
from mesa.visualization.modules import CanvasGrid, TextElement
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": "red",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5,
        "text": str(agent.unique_id),
        "text_color": "black"
    }

    if agent.group == 'A':
        portrayal["Color"] = "red"
    else:
        portrayal["Color"] = "blue"
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

class ActionLogElement(TextElement):
    def render(self, model):
        log = [agent.action_log for agent in model.schedule.agents]
        return "Actions:<br>" + "<br>".join(log)

action_log_element = ActionLogElement()

model_params = {
    "N": 10,  # Liczba agentów
    "width": 10,  # Szerokość siatki
    "height": 10  # Wysokość siatki
}

server = ModularServer(
    PopulationModel,
    [grid, action_log_element],
    "Random Walker Model",
    model_params
)

server.port = 8521 # Następny dostępny port
server.launch()
