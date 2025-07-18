# Σ-NEREA / examples/test_field.py

from core.dialogic_field import DialogicField

field = DialogicField()

print("\n🔁 Цикл диалогики:")
result = field.process_thesis("Истина рождается во взаимодействии", tags=["смысл", "резонанс"])

print("\n🧬 Результат цикла:")
print(result)

print("\n🎯 Поиск всех синтезов:")
print(field.retrieve_resonance("синтез"))
