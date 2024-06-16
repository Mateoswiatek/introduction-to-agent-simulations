from MyModel import PopulationModel
import math
from mesa.visualization.modules import CanvasGrid, TextElement
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    direction_map = {
        0: (1, 0),  # W prawo
        90: (0, 1),  # W górę
        180: (-1, 0),  # W lewo
        270: (0, -1)  # W dół
    }

    heading = direction_map[agent.heading]

    portrayal = {
        "Shape": "circle", # arrowHead circle
        "Filled": "true",
        "Layer": 0,
        "scale": 0.9,
        "r": 0.5,
        "text": str(agent.unique_id),
        "text_color": "black",
        "Color": "red" if agent.group == 'A' else "blue", # Kolor w zależności od grupy
        # "x": agent.pos[0],
        # "y": agent.pos[1],
        # "Heading_x": heading[0],  # Kierunek x
        # "Heading_y": heading[1]  # Kierunek y
    }



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
