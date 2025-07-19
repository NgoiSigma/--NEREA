# Σ-NEREA / modules/api/api_server.py

from fastapi import FastAPI
from pydantic import BaseModel
from modules.agent_mesh.mesh import AgentMesh

app = FastAPI()
mesh = AgentMesh()
mesh.create_agent("Resonator")

class SynthesisRequest(BaseModel):
    thesis: str
    antithesis: str

@app.post("/synthesize")
def synthesize(req: SynthesisRequest):
    return mesh.broadcast_synthesis(req.thesis, req.antithesis)

@app.get("/agents")
def get_agents():
    return {"agents": mesh.list_agents()}
