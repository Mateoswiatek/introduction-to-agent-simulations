from MyModel import PopulationModel
from mesa.visualization.modules import CanvasGrid
from mesa.visualization.ModularVisualization import ModularServer

def agent_portrayal(agent):
    portrayal = {
        "Shape": "circle",
        "Color": "red",
        "Filled": "true",
        "Layer": 0,
        "r": 0.5
    }
    return portrayal

grid = CanvasGrid(agent_portrayal, 10, 10, 500, 500)

model_params = {
    "N": 10,  # Liczba agentów
    "width": 10,  # Szerokość siatki
    "height": 10  # Wysokość siatki
}

server = ModularServer(
    PopulationModel,
    [grid],
    "Random Walker Model",
    model_params
)

server.port = 8521 # Następny dostępny port
server.launch()
