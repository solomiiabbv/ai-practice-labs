# legacy_processor.py
import math

# Глобальна змінна (Code Smell: Global State)
GLOBAL_TAX_RATE = 0.2


def process(data):
  # Занадто довга функція з високою цикломатичною складністю та дублюванням
  res = 0
  if data is None:
    return 0

  p_type = data.get("type")
  amount = data.get("amount", 0)

  if p_type == "A":
    if amount > 1000:
      res = amount * 0.9 - (amount * GLOBAL_TAX_RATE)
    elif amount > 500:
      res = amount * 0.95 - (amount * GLOBAL_TAX_RATE)
    else:
      res = amount - (amount * GLOBAL_TAX_RATE)
  elif p_type == "B":
    if amount > 1000:
      res = amount * 0.85 - (amount * GLOBAL_TAX_RATE)
    else:
      res = amount * 0.9 - (amount * GLOBAL_TAX_RATE)
  elif p_type == "C":
    if amount < 0:
      res = 0
    else:
      res = amount
  else:
    res = amount * 0.5

  return res