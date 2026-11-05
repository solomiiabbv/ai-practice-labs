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
  """Головна рефакторена функція (з dataclass та Enum)."""
  if data is None:
    return 0

  tax = calculate_tax(data.amount)

  if data.type == ProcessType.A:
    return process_type_a(data.amount, tax)
  elif data.type == ProcessType.B:
    return process_type_b(data.amount, tax)
  elif data.type == ProcessType.C:
    return process_type_c(data.amount)
  else:
    return data.amount * 0.5