# Σ-NEREA / core/dialogic_field.py

from core.fdl_logic_engine import FDLLogicEngine
from core.archai_memory import ArchaiMemory

class DialogicField:
    def __init__(self):
        self.logic = FDLLogicEngine()
        self.memory = ArchaiMemory()
        self.context = {}

    def process_thesis(self, thesis: str, tags: list = None) -> dict:
        self.logic.input_thesis(thesis)
        antithesis = self.logic.generate_antithesis()
        synthesis = self.logic.synthesize()
        result = self.logic.emit()

        # Сохраняем все три фазы в память
        self.memory.store(thesis, f"Тезис → {thesis}", tags or ["тезис"])
        self.memory.store(antithesis, f"Антитезис → {antithesis}", tags or ["антитезис"])
        self.memory.store(synthesis, f"Синтез → {synthesis}", tags or ["синтез"])

        self.context = result
        return result

    def retrieve_resonance(self, tag: str) -> dict:
        return self.memory.search_by_tag(tag)

    def current_state(self) -> dict:
        return self.context
