# Σ-NEREA / interface/agent_hub.py

from core.fdl_core import AvatarusSigma

class AgentHub:
    def __init__(self):
        self.agents = {}

    def create_agent(self, name):
        agent = AvatarusSigma(name=name)
        self.agents[name] = agent
        return f"✅ Agent '{name}' initialized."

    def route_synthesis(self, name, thesis, antithesis):
        if name not in self.agents:
            return f"⚠️ Agent '{name}' not found."
        return self.agents[name].inject_node(thesis, antithesis)

    def list_agents(self):
        return list(self.agents.keys())
