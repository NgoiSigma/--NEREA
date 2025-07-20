# Σ-NEREA / network/linker.py

import requests

class FDLLinker:
    def __init__(self, endpoint):
        self.endpoint = endpoint

    def send_synthesis(self, thesis, antithesis):
        payload = {"thesis": thesis, "antithesis": antithesis}
        try:
            response = requests.post(f"{self.endpoint}/receive", json=payload)
            return response.text
        except Exception as e:
            return f"Ошибка связи: {e}"
