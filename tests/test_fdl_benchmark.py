from core.fdl_core import AvatarusSigma
from modules.benchmark.fdl_benchmark import FDLBenchmark

agent = AvatarusSigma()
agent.inject_node("Мир", "Хаос")
agent.inject_node("Вера", "Сомнение")

bench = FDLBenchmark(agent)
print(bench.report())
