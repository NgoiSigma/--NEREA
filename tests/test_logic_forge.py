# Σ-NEREA / tests/test_logic_forge.py

from modules.logic_forge.forge import LogicForge

forge = LogicForge()
token = forge.forge_token("Исток", "Забвение", "Память как структура света")
print(f"Token saved to: {token}")
