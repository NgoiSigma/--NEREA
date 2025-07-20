# Σ-NEREA / compiler/fdl_exporter.py

import json
import networkx as nx

class FDLExporter:
    def __init__(self, agent):
        self.agent = agent

    def to_json(self, path="fdl_output.json"):
        data = [{
            "thesis": n.thesis,
            "antithesis": n.antithesis,
            "synthesis": n.synthesis
        } for n in self.agent.field.nodes]
        with open(path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)

    def to_graphml(self, path="fdl_graph.graphml"):
        G = nx.DiGraph()
        for i, node in enumerate(self.agent.field.nodes):
            G.add_node(i, synthesis=node.synthesis)
            G.add_edge(i, i+1)
        nx.write_graphml(G, path)

    def to_text(self, path="fdl_scroll.txt"):
        lines = [f"{n.thesis} ⊕ {n.antithesis} = {n.synthesis}" for n in self.agent.field.nodes]
        with open(path, "w", encoding="utf-8") as f:
            f.write("\n".join(lines))
