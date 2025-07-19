from core.fdl_core import AvatarusSigma
from modules.compiler.compiler import FDLCompiler

agent = AvatarusSigma()
agent.inject_node("Цель", "Средство")
agent.inject_node("Знание", "Опыт")

compiler = FDLCompiler()
print("--- YAML ---")
print(compiler.compile_to_yaml(agent.field))

print("--- JSON ---")
print(compiler.compile_to_json(agent.field))
