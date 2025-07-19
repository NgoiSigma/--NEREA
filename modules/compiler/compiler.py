# Σ-NEREA / modules/compiler/compiler.py

import yaml
import json

class FDLCompiler:
    def compile_to_yaml(self, field):
        data = [
            {"thesis": n.thesis, "antithesis": n.antithesis, "synthesis": n.synthesis}
            for n in field.nodes
        ]
        return yaml.dump(data, allow_unicode=True)

    def compile_to_json(self, field):
        data = [
            {"thesis": n.thesis, "antithesis": n.antithesis, "synthesis": n.synthesis}
            for n in field.nodes
        ]
        return json.dumps(data, indent=2, ensure_ascii=False)
