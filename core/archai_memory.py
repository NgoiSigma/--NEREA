# Σ-NEREA / core/archai_memory.py

class ArchaiMemory:
    def __init__(self):
        self.vault = {}
        self.tags = {}

    def store(self, key: str, value: str, tags: list = None) -> None:
        self.vault[key] = value
        if tags:
            self.tags[key] = tags
        print(f"🗃️ Записано в память: [{key}]")

    def retrieve(self, key: str) -> str:
        return self.vault.get(key, "⛔ Пусто")

    def search_by_tag(self, tag: str) -> dict:
        results = {
            k: self.vault[k] for k, v in self.tags.items() if tag in v
        }
        print(f"🔎 Найдено по тегу '{tag}': {list(results.keys())}")
        return results

    def all_entries(self) -> dict:
        return self.vault
