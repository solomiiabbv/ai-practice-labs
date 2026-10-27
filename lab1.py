import os
from dotenv import load_dotenv
from google import genai
from google.genai import types

load_dotenv()
client = genai.Client()

SYSTEM_INSTRUCTION = (
    "Ти досвідчений Python-розробник. Пиши код для Python 3.10+, "
    "з анотаціями типів, docstring у стилі Google та явною "
    "обробкою винятків. Відповідай лише кодом."
)

print("=== ТРИ ПАТТЕРНИ ПРОМПТ-ІНЖИНІРИНГУ ===")

# 1. Zero-Shot Prompt
print("\n[1] Виконується Zero-Shot запит...")
response_zeroshot = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents='Напиши функцію на Python для розрахунку кінцевої ціни товару зі знижкою calculate_discount. Передбач генерацію ValueError для некоректних аргументів.',
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.2,
    )
)
print("--- Результат Zero-Shot ---")
print(response_zeroshot.text)

# 2. Few-Shot Prompt
print("\n[2] Виконується Few-Shot запит...")
few_shot_prompt = (
    "Напиши функцію calculate_discount на Python з огляду на приклади:\n"
    "Приклад 1: price = 1000, discount = 10 -> 900.0\n"
    "Приклад 2: price = 500, discount = 20 -> 400.0\n"
    "Передбач генерацію ValueError для невалідних вхідних даних (від'ємна ціна або знижка поза межами 0-100%)."
)
response_fewshot = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=few_shot_prompt,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.2,
    )
)
print("--- Результат Few-Shot ---")
print(response_fewshot.text)

# 3. Chain-of-Thought Prompt
print("\n[3] Виконується Chain-of-Thought (CoT) запит...")
cot_prompt = (
    "Спочатку покроково розпиши логіку розрахунку знижки та перевірки граничних випадків "
    "(від'ємна ціна, знижка поза межами 0-100%), а потім надай повний якісний код функції calculate_discount на Python."
)
response_cot = client.models.generate_content(
    model='models/gemini-3.5-flash',
    contents=cot_prompt,
    config=types.GenerateContentConfig(
        system_instruction=SYSTEM_INSTRUCTION,
        temperature=0.2,
    )
)
print("--- Результат Chain-of-Thought ---")
print(response_cot.text)