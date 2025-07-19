# Σ-NEREA / examples/test_meta_action.py

from core.meta_action_engine import MetaActionEngine

engine = MetaActionEngine()

samples = [
    ("SYNTH[Свобода ⊕ Структура]", "Когнитивный Резонанс"),
    ("SYNTH[Память ⊕ Поток]", "Мнемонический Резонанс"),
    ("SYNTH[Жизнь ⊕ Тишина]", "Экзистенциальный Резонанс"),
    ("SYNTH[Скорость ⊕ Масса]", "Нейтральный Резонанс"),
]

for synth, rtype in samples:
    act = engine.decide_action(synth, rtype)
    print(f"\n⭢ {act}")
