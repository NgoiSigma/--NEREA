# Σ-NEREA / core/visual_core.py

import networkx as nx
import matplotlib.pyplot as plt

class VisualCore:
    def __init__(self, dialogic_field):
        self.field = dialogic_field

    def render_field(self):
        G = nx.DiGraph()
        for node in self.field.nodes:
            G.add_node(node.thesis, color='skyblue')
            G.add_node(node.antithesis, color='lightcoral')
            G.add_node(node.synthesis, color='palegreen')
            G.add_edge(node.thesis, node.synthesis)
            G.add_edge(node.antithesis, node.synthesis)

        colors = [G.nodes[n].get('color', 'gray') for n in G.nodes]
        pos = nx.spring_layout(G, seed=42)
        nx.draw(G, pos, with_labels=True, node_color=colors, node_size=1200, font_size=8)
        plt.title("Σ-Dialogic Field Map")
        plt.show()
