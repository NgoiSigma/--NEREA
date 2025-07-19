from core.fdl_core import AvatarusSigma
from core.visual_core import VisualCore

agent = AvatarusSigma()
agent.inject_node("Информация", "Перегрузка")
agent.inject_node("Воля", "Условие")
agent.inject_node("Гармония", "Сопротивление")

visualizer = VisualCore(agent.field)
visualizer.render_field()
