# Σ-NEREA / modules/api_server/main.py

from fastapi import FastAPI, Body
from pydantic import BaseModel
from core.fdl_core import AvatarusSigma
from core.visual_core import VisualCore

agent = AvatarusSigma()
app = FastAPI(title="Σ-NEREA FDL API", version="0.1")

class FDLRequest(BaseModel):
    thesis: str
    antithesis: str

@app.post("/fdl/synthesize")
def synthesize_node(req: FDLRequest):
    synth = agent.inject_node(req.thesis, req.antithesis)
    return {
        "synthesis": synth,
        "field_size": len(agent.field.nodes)
    }

@app.get("/fdl/resonance_map")
def render_dialogic_field():
    try:
        viz = VisualCore(agent.field)
        viz.render_field()
        return {"status": "Rendered"}
    except Exception as e:
        return {"error": str(e)}
