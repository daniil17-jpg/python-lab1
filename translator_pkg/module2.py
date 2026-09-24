import sys

if sys.version_info >= (3, 13):
    print(f"[Попередження]: Поточна версія Python {sys.version_info.major}.{sys.version_info.minor} занадто висока для googletrans v3!")

import sys
from googletrans import Translator, LANGUAGES

# Перевірка версії Python (повинна бути >= 3.13)
if sys.version_info < (3, 13):
    print(f"[Попередження]: Поточна версія Python {sys.version_info.major}.{sys.version_info.minor}. Для модуля gtrans3 потрібна версія 3.13 або вище!")

translator = Translator()

def TransLate(text: str, scr: str, dest: str) -> str:
    """Повертає текст перекладений на задану мову, або повідомлення про помилку."""
    try:
        if scr == 'auto':
            translated = translator.translate(text, dest=dest)
        else:
            translated = translator.translate(text, src=scr, dest=dest)
        return translated.text
    except Exception as e:
        return f"[Помилка]: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри для заданого тексту."""
    try:
        detection = translator.detect(text)
        lang = detection.lang
        confidence = detection.confidence
        
        if set == "lang":
            return lang
        elif set == "confidence":
            return str(confidence)
        else:
            return f"Мова: {lang}, Коефіцієнт довіри: {confidence}"
    except Exception as e:
        return f"[Помилка]: {e}"

def CodeLang(lang: str) -> str:
    """Повертає код мови за назвою або назву за кодом."""
    lang_lower = lang.lower()
    if lang_lower in LANGUAGES:
        return LANGUAGES[lang_lower].capitalize()
    
    for code, name in LANGUAGES.items():
        if name.lower() == lang_lower:
            return code
            
    return "[Помилка]: Мову не знайдено"

def LanguageList(out: str = "screen", text: str = "") -> str:
    """Виводить таблицю мов на екран або у файл і виконує переклад тексту за наявності."""
    try:
        lines = []
        header = f"{'N':<3} {'Language':<15} {'ISO-639 code':<15}"
        if text:
            header += " Text"
        lines.append(header)
        lines.append("-" * len(header))
        
        for idx, (code, name) in enumerate(LANGUAGES.items(), start=1):
            row = f"{idx:<3} {name.capitalize():<15} {code:<15}"
            if text:
                translated_text = TransLate(text, 'auto', code)
                row += f" {translated_text}"
            lines.append(row)
            
        result_str = "\n".join(lines)
        
        if out == "file":
            with open("languages_output_v3.txt", "w", encoding="utf-8") as f:
                f.write(result_str)
        else:
            print(result_str)
            
        return "Ok"
    except Exception as e:
        return f"[Помилка]: {e}"