# Σ-NEREA / tests/test_vault.py

from modules.vault.vault import DataVault

vault = DataVault("test_vault.json")
vault.load()

vault.add_entry("Природа", "Техника", "Синтез: Биомеханика")
vault.add_entry("Память", "Поток", "Синтез: Хронотоп")

print("Все записи:")
for e in vault.entries:
    print(f"- {e['timestamp']} | {e['synthesis']}")

print("\nФильтр по 'Хроно':")
matches = vault.filter_by_keyword("Хроно")
for m in matches:
    print(f"→ {m['synthesis']}")
