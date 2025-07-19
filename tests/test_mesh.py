from modules.agent_mesh.mesh import AgentMesh

mesh = AgentMesh()
mesh.create_agent("Герменевт")
mesh.create_agent("Архитектор")

results = mesh.broadcast_synthesis("Интуиция", "Структура")
for name, syn in results.items():
    print(f"{name} → {syn}")
