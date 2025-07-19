# === МОДУЛЬ 4: Резонансный Анализ ===

class SemanticResonator:
    def __init__(self, archetypal_memory=None):
        self.memory = archetypal_memory

    def analyze(self, synthesis):
        base_score = sum(ord(c) for c in synthesis) % 144
        resonance_type = self.detect_type(synthesis)
        return {
            "synthesis": synthesis,
            "resonance_level": f"{base_score} Hz",
            "type": resonance_type
        }

    def detect_type(self, synthesis):
        if "Свобода" in synthesis or "воля" in synthesis.lower():
            return "Когнитивный Резонанс"
        elif "память" in synthesis.lower() or "архетип" in synthesis.lower():
            return "Мнемонический Резонанс"
        elif "дух" in synthesis.lower() or "жизнь" in synthesis.lower():
            return "Экзистенциальный Резонанс"
        else:
            return "Нейтральный Резонанс"
