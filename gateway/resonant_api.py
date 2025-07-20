# Σ-NEREA / gateway/resonant_api.py

from fastapi import FastAPI
from pydantic import BaseModel
from interface.agent_hub import AgentHub

app = FastAPI()
hub = AgentHub()

class Input(BaseModel):
    name: str
    thesis: str
    antithesis: str

@app.post("/inject")
def inject(input: Input):
    return {"synthesis": hub.route_synthesis(input.name, input.thesis, input.antithesis)}

@app.get("/agents")
def agents():
    return {"available": hub.list_agents()}

@app.post("/create")
def create(input: Input):
    return {"status": hub.create_agent(input.name)}
