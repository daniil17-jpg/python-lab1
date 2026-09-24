from translator_pkg import module3

def run_demo():
    print("=== Демонстрація роботи модуля 3 (Deep Translator) ===")
    
    sample_text = "Астрономи постійно знаходять нові екзопланети."
    
    # Переклад на іспанську
    translated = module3.TransLate(sample_text, "uk", "es")
    print(f"Оригінал: {sample_text}")
    print(f"Переклад (es): {translated}")
    
    # Визначення мови через langdetect
    detected = module3.LangDetect(sample_text, "confidence")
    print(f"Коефіцієнт довіри мови: {detected}")

if __name__ == "__main__":
    run_demo()