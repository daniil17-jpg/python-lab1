import asyncio
from translator_pkg import module1

async def run_demo():
    print("=== Демонстрація роботи модуля 1 (Googletrans v4) ===")
    
    sample_text = "Космічні дослідження відіграють важливу роль."
    
    # Переклад на англійську
    translated = await module1.TransLate(sample_text, "uk", "en")
    print(f"Оригінал: {sample_text}")
    print(f"Переклад (en): {translated}")
    
    # Визначення мови
    detected = await module1.LangDetect(sample_text, "all")
    print(f"Визначення мови: {detected}")
    
    # Перевірка кодування мови
    print(f"Код для 'Ukrainian': {module1.CodeLang('Ukrainian')}")

if __name__ == "__main__":
    asyncio.run(run_demo())