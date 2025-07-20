# Σ-NEREA / runner/cli_runner.py

from core.fdl_core import AvatarusSigma
from modules.executor.synaptic_executor import SynapticExecutor
from modules.shield.semantic_shield import SemanticShield

agent = AvatarusSigma()
executor = SynapticExecutor()
shield = SemanticShield()

print("Σ-NEREA CLI Активна. Введите тезис и антитезис:")

while True:
    thesis = input("Тезис: ")
    antithesis = input("Антитезис: ")
    
    synthesis = agent.inject_node(thesis, antithesis)
    print(f"⚙️ Синтез: {synthesis}")
    
    audit = shield.audit(synthesis)
    print(f"🛡️ Анализ: {audit}")
    
    result = executor.execute(synthesis)
    print(f"⚡ Действие: {result}\n")
