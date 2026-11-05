# test_legacy.py
import pytest
from legacy_processor import process as legacy_process

# Набір репрезентативних тестових даних (включно з граничними випадками)
CASES = [
    {"type": "A", "amount": 1200},  # тип А, велика сума (>1000)
    {"type": "A", "amount": 600},  # тип А, середня сума (>500)
    {"type": "A", "amount": 100},  # тип А, мала сума (<=500)
    {"type": "B", "amount": 1500},  # тип B, велика сума (>1000)
    {"type": "B", "amount": 300},  # тип B, мала сума (<=1000)
    {"type": "C", "amount": -10},  # тип C з від'ємною сумою (граничний випадок)
    {"type": "C", "amount": 500},  # тип C зі звичайною сумою
    {"type": "X", "amount": 200},  # невідомий тип (else блок)
    None,  # нульовий вхід (edge case)
]


@pytest.mark.parametrize("payload", CASES)
def test_behavior_is_unchanged(payload):
  """Golden master тест: перевіряє, що функція працює стабільно.

  На цьому етапі ми порівнюємо функцію саму з собою, а після рефакторингу
  порівнюватимемо новий код зі старим.
  """
  # Оскільки новий модуль рефакторингу ми ще не створили,
  # поки що перевіряємо стабільність легасі-коду
  assert legacy_process(payload) == legacy_process(payload)