# Σ-NEREA / core/interface_shell.py

from core.meta_action_engine import MetaActionEngine
from core.dialogic_field import DialogicField
from core.archai_memory import ArchaiMemory
from core.fdl_node import FDLNode
from core.semantic_resonator import SemanticResonator

class InterfaceShell:
    def __init__(self, agent):
        self.agent = agent

    def handle_input(self, user_input):
        if "::" in user_input:
            thesis, antithesis = map(str.strip, user_input.split("::"))
        else:
            thesis, antithesis = user_input, "Неопределённость"

        synthesis = self.agent.inject_node(thesis, antithesis)
        return synthesis

    def welcome(self):
        return (
            "\n🌀 Добро пожаловать в Σ‑NEREA InterfaceShell\n"
            "Формат: 'Тезис :: Антитезис'\n"
            "Пример: 'Память :: Поток'\n"
            "Для выхода: Ctrl+C\n"
        )
