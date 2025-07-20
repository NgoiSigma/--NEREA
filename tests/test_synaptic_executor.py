from modules.executor.synaptic_executor import SynapticExecutor

def log_action(s):
    print(f"🔥 LOGIC FIRE: {s}")
    return "Action complete"

executor = SynapticExecutor()
executor.register_action("Свет", log_action)
result = executor.execute("SYNTH[Память ⊕ Свет]")
print(result)
