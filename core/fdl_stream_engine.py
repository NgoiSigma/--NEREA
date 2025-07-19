# Σ-NEREA / core/fdl_stream_engine.py

from datetime import datetime

class FDLStreamEngine:
    def __init__(self, log_path="logs/fdl_stream.log"):
        self.log_path = log_path
        self.buffer = []

    def log_event(self, synthesis, resonance_type, action):
        timestamp = datetime.utcnow().isoformat()
        entry = f"[{timestamp}] | SYNTH: {synthesis} | RESONANCE: {resonance_type} | ACTION: {action}"
        self.buffer.append(entry)
        self._write(entry)

    def _write(self, entry):
        with open(self.log_path, "a", encoding="utf-8") as log_file:
            log_file.write(entry + "\n")

    def export(self):
        return self.buffer
