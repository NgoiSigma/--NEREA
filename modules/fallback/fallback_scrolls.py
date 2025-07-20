# Σ-NEREA / modules/fallback/fallback_scrolls.py

class FallbackScrolls:
    def __init__(self):
        self.scrolls = {
            "no_context": "Когда смысл ускользает — открой Путь через Точку Входа.",
            "conflict_loop": "Замкнутость — признак перехода. Попробуй сменить грань.",
            "null_synthesis": "Синтез невозможен. Возможно, ты смотришь в зеркало без отражения."
        }

    def get_scroll(self, key):
        return self.scrolls.get(key, "Загадка за пределами свитков.")
