# Σ-NEREA / modules/dashboard/graph_builder.py

import networkx as nx
import matplotlib.pyplot as plt

def build_logic_graph(agent, save_path="dashboard.png"):
    G = nx.DiGraph()
    for node in agent.field.nodes:
        G.add_edge(node.thesis, node.synthesis)
        G.add_edge(node.antithesis, node.synthesis)

    plt.figure(figsize=(10, 6))
    nx.draw(G, with_labels=True, node_color='lightblue', font_size=10, node_size=2000)
    plt.title("FDL Logic Network")
    plt.savefig(save_path)
    plt.close()
