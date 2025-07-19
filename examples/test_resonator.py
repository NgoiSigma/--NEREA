# Σ-NEREA / examples/test_resonator.py

from core.semantic_resonator import SemanticResonator

resonator = SemanticResonator()

synthesis_1 = "SYNTH[Свобода ⊕ Структура]"
synthesis_2 = "SYNTH[Память ⊕ Поток]"
synthesis_3 = "SYNTH[Жизнь ⊕ Тишина]"
synthesis_4 = "SYNTH[Скорость ⊕ Масса]"

for s in [synthesis_1, synthesis_2, synthesis_3, synthesis_4]:
    result = resonator.analyze(s)
    print(f"\n📡 {s}")
    print(f"→ Уровень: {result['resonance_level']}")
    print(f"→ Тип: {result['type']}")
