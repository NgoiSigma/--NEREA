# Σ-NEREA / modules/executor/synaptic_executor.py

class SynapticExecutor:
    def __init__(self, action_map=None):
        self.action_map = action_map or {}

    def register_action(self, pattern, callback):
        self.action_map[pattern] = callback

    def execute(self, synthesis):
        for pattern, action in self.action_map.items():
            if pattern in synthesis:
                return action(synthesis)
        return f"[NO ACTION] → {synthesis}"
