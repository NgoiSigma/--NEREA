# Σ-NEREA / modules/benchmark/fdl_benchmark.py

class FDLBenchmark:
    def __init__(self, agent):
        self.agent = agent

    def coherence_score(self):
        synths = [node.synthesis for node in self.agent.field.nodes]
        if not synths:
            return 0
        unique_chars = len(set("".join(synths)))
        return round(unique_chars / len(synths), 2)

    def report(self):
        score = self.coherence_score()
        if score > 5:
            return f"📈 Высокая семантическая плотность: {score}"
        elif score > 3:
            return f"🧭 Умеренный когерентный поток: {score}"
        return f"⚠️ Разреженность смыслов: {score}"
