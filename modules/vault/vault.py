# Σ-NEREA / modules/vault/vault.py

import json
from datetime import datetime

class DataVault:
    def __init__(self, filepath="vault.json"):
        self.filepath = filepath
        self.entries = []

    def add_entry(self, thesis, antithesis, synthesis):
        entry = {
            "timestamp": datetime.utcnow().isoformat(),
            "thesis": thesis,
            "antithesis": antithesis,
            "synthesis": synthesis
        }
        self.entries.append(entry)
        self.save()

    def save(self):
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(self.entries, f, ensure_ascii=False, indent=2)

    def load(self):
        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                self.entries = json.load(f)
        except FileNotFoundError:
            self.entries = []

    def filter_by_keyword(self, keyword):
        return [e for e in self.entries if keyword in e["synthesis"]]
