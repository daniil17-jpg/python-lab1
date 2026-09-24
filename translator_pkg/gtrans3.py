from translator_pkg import module2

def run_demo():
    print("=== Демонстрація роботи модуля 2 (Googletrans v3) ===")
    
    sample_text = "Сучасні телескопи дозволяють бачити далекі галактики."
    
    # Переклад на німецьку
    translated = module2.TransLate(sample_text, "uk", "de")
    print(f"Оригінал: {sample_text}")
    print(f"Переклад (de): {translated}")
    
    # Визначення мови
    detected = module2.LangDetect(sample_text, "lang")
    print3 = f"Визначена мова: {detected}"
    print(print3)

if __name__ == "__main__":
    run_demo()