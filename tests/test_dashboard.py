from core.fdl_core import AvatarusSigma
from modules.dashboard.graph_builder import build_logic_graph

agent = AvatarusSigma("Пифагор")
agent.inject_node("Целое", "Частное")
agent.inject_node("Материя", "Смысл")

build_logic_graph(agent, "tests/fdl_graph_output.png")
print("Граф сохранён.")
