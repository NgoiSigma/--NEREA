# tests/test_reflector.py

from core.fdl_core import AvatarusSigma
from modules.reflector.reflector import SigmaReflector

agent = AvatarusSigma()
agent.inject_node("Явление", "Скрытие")
agent.inject_node("Свет", "Свет")  # конфликт

reflector = SigmaReflector(agent.field)
print(reflector.summarize_field())
