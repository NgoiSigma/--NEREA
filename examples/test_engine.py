# Σ-NEREA / examples/test_engine.py

from core.fdl_logic_engine import FDLLogicEngine

engine = FDLLogicEngine()
engine.input_thesis("Порядок рождается из напряжения")
engine.generate_antithesis()
engine.synthesize()
result = engine.emit()

print("\n📘 Итоговый результат логического цикла:")
print(result)
