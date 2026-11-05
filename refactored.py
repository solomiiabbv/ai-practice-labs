# refactored.py
from dataclasses import dataclass
from enum import Enum
import math


class ProcessType(Enum):
  """Перелік допустимих типів обробки (замість магічних рядків)."""

  A = "A"
  B = "B"
  C = "C"


@dataclass
class ProcessData:
  """Датаклас для структурованого та типізованого зберігання вхідних даних."""

  type: ProcessType
  amount: float


GLOBAL_TAX_RATE = 0.2


def calculate_tax(amount: float) -> float:
  """Обчислює податок на основі глобальної ставки."""
  return amount * GLOBAL_TAX_RATE


def process_type_a(amount: float, tax: float) -> float:
  """Логіка розрахунку для типу A з типізацією."""
  if amount > 1000:
    return amount * 0.9 - tax
  elif amount > 500:
    return amount * 0.95 - tax
  else:
    return amount - tax


def process_type_b(amount: float, tax: float) -> float:
  """Логіка розрахунку для типу B з типізацією."""
  if amount > 1000:
    return amount * 0.85 - tax
  else:
    return amount * 0.9 - tax


def process_type_c(amount: float) -> float:
  """Логіка розрахунку для типу C з типізацією."""
  if amount < 0:
    return 0
  else:
    return amount


def process(data: ProcessData | None) -> float:
  """Головна рефакторена функція (Крок 3: із сучасним match-case)."""
  match data:
    case None:
      return 0
    case ProcessData(type=ProcessType.A, amount=amt):
      return process_type_a(amt, calculate_tax(amt))
    case ProcessData(type=ProcessType.B, amount=amt):
      return process_type_b(amt, calculate_tax(amt))
    case ProcessData(type=ProcessType.C, amount=amt):
      return process_type_c(amt)
    case _:
      return getattr(data, "amount", 0) * 0.5