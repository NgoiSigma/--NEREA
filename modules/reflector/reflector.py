# Σ-NEREA / modules/reflector/reflector.py

class SigmaReflector:
    def __init__(self, dialogic_field):
        self.field = dialogic_field

    def detect_loops(self):
        seen = set()
        loops = []
        for node in self.field.nodes:
            key = (node.thesis, node.antithesis)
            if key in seen:
                loops.append(key)
            seen.add(key)
        return loops

    def detect_conflicts(self):
        # Простейшая проверка на "противостояние"
        conflicts = []
        for node in self.field.nodes:
            if node.thesis.lower() == node.antithesis.lower():
                conflicts.append(node)
        return conflicts

    def summarize_field(self):
        return {
            "nodes": len(self.field.nodes),
            "loops": self.detect_loops(),
            "conflicts": [str(n) for n in self.detect_conflicts()]
        }
