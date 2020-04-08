from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.modules import CanvasGrid, ChartModule
from mesa.visualization.UserParam import UserSettableParameter

from agents import Oil,Boat,Land, Bound
from model import OilSpread


def Spread_Oil_portrayal(agent):
    
    if agent is None:
        return
    portrayal = {"Shape": "circle", "r": 0.5, "Filled": "true", "Layer": 0}

    if type(agent) is Oil:
        portrayal["Color"] = ["#010101", "#999900"]
        portrayal["stroke_color"] = "#000000"
        portrayal["text"] = round(agent.qnt, 1)
        portrayal["text_color"] = "yellow"
    if type(agent) is Boat:
        portrayal["Color"] = ["#00FFFF", "#FFFFFF"]
        portrayal["stroke_color"] = "#FFFFFF"
        portrayal["text"] = round(agent.power, 1)
        portrayal["text_color"] = "red"
    if type(agent) is Land:
        portrayal["Color"] = ["#654321", "#654321"]
        portrayal["stroke_color"] = "#FFFFFF"
        portrayal["text"] = round(agent.status, 1)
        portrayal["text_color"] = "white"
    if type(agent) is Bound:
        portrayal["Color"] = ["#0000FF", "#0000FF"]
        portrayal["stroke_color"] = "#FFFFFF"
    return portrayal


canvas_element = CanvasGrid(Spread_Oil_portrayal, 20, 20, 500, 500)
chart_element = ChartModule([{"Label": "Oil", "Color": "#000000"}])

model_params = {"initial_macchie": UserSettableParameter('slider', 'quantità di macchie di petrolio', 1, 0, 10),
                "initial_land": UserSettableParameter('slider', 'quantità di terra', 20, 0, 20),
                "initial_barche": UserSettableParameter('slider', 'quantità di barche rimuovi petrolio', 1, 0, 10),
                "power_boat": UserSettableParameter('slider', 'Quantità di petrolio raccolto da una barca', 10, 1, 10),
                "qnt": UserSettableParameter('slider', 'Quantità iniziale', 10, 1, 1000),
                "qnt_prop": UserSettableParameter('slider', 'Initial quantitaty propagated', 50, 0, 100)}

server = ModularServer(OilSpread, [canvas_element, chart_element], "propagazione petrolio", model_params)
server.port = 8521
