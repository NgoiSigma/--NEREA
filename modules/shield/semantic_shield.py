# Σ-NEREA / modules/shield/semantic_shield.py

class SemanticShield:
    def __init__(self):
        self.stop_phrases = ["...", "???", "!!", "undefined", "null", "confused"]

    def validate(self, synthesis: str) -> bool:
        return not any(phrase in synthesis.lower() for phrase in self.stop_phrases)

    def audit(self, synthesis: str) -> str:
        if self.validate(synthesis):
            return "✅ Смысл ясен. Контекст целостен."
        return "⚠️ Обнаружен разрыв. Необходима рекалибровка."
