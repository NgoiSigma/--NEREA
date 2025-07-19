# Σ-NEREA / modules/logic_forge/forge.py

from datetime import datetime

class LogicForge:
    def __init__(self, output_dir="forged_tokens/"):
        self.output_dir = output_dir

    def forge_token(self, thesis, antithesis, synthesis):
        now = datetime.utcnow().strftime("%Y-%m-%d_%H%M%S")
        token_name = f"FDL_{now}.md"
        body = self.generate_markdown(thesis, antithesis, synthesis)

        with open(f"{self.output_dir}{token_name}", "w", encoding="utf-8") as f:
            f.write(body)
        return token_name

    def generate_markdown(self, thesis, antithesis, synthesis):
        return f"""# ⊕ FDL-Токен

**Тезис:** {thesis}  
**Антитезис:** {antithesis}  
**Синтез:** {synthesis}  

> "Смысл рождается во встрече противоположностей."  
_— Λ‑Logic Forge_

⟲ Скомпилировано: {datetime.utcnow().isoformat()} UTC  
"""
