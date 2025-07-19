# Σ-NEREA / core/meta_action_engine.py

class MetaActionEngine:
    def __init__(self):
        self.history = []

    def decide_action(self, synthesis: str, resonance_type: str) -> str:
        if resonance_type == "Когнитивный Резонанс":
            action = f"[Оповещение]: Новая мысль для обсуждения: {synthesis}"
        elif resonance_type == "Мнемонический Резонанс":
            action = f"[Запись в хронику]: Архетип найден — {synthesis}"
        elif resonance_type == "Экзистенциальный Резонанс":
            action = f"[Переход к ритуалу]: Инициировать процесс осознания: {synthesis}"
        else:
            action = f"[Логирование]: Нейтральный резонанс — {synthesis}"

        self.history.append((synthesis, resonance_type, action))
        return action

    def get_history(self):
        return self.history
