from modules.shield.semantic_shield import SemanticShield

shield = SemanticShield()
print(shield.audit("SYNTH[Свет ⊕ Тьма]"))
print(shield.audit("null response ???"))
