# Σ-NEREA / examples/test_memory.py

from core.archai_memory import ArchaiMemory

memory = ArchaiMemory()
memory.store("Начало", "В начале был Тезис", tags=["генезис", "основа"])
memory.store("Конец", "Эмиссия завершает цикл", tags=["завершение", "эмиссия"])

print("\n📦 Тестовое извлечение:")
print(memory.retrieve("Начало"))

print("\n🔖 Поиск по тегу 'эмиссия':")
memory.search_by_tag("эмиссия")

print("\n📚 Все записи:")
print(memory.all_entries())
