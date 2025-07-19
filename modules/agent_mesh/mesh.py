# Σ-NEREA / modules/agent_mesh/mesh.py

from core.fdl_core import AvatarusSigma

class AgentMesh:
    def __init__(self):
        self.agents = {}

    def create_agent(self, name):
        agent = AvatarusSigma(name)
        self.agents[name] = agent
        return agent

    def broadcast_synthesis(self, thesis, antithesis):
        results = {}
        for name, agent in self.agents.items():
            synthesis = agent.inject_node(thesis, antithesis)
            results[name] = synthesis
        return results

    def list_agents(self):
        return list(self.agents.keys())
