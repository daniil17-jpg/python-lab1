from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs, DetectorFactory
from googletrans import LANGUAGES

# Щоб результати detect були стабільними
DetectorFactory.seed = 0

def TransLate(text: str, scr: str, dest: str) -> str:
    """Повертає текст перекладений на задану мову через deep_translator."""
    try:
        source_lang = 'auto' if scr == 'auto' else scr
        translated = GoogleTranslator(source=source_lang, target=dest).translate(text)
        return translated
    except Exception as e:
        return f"[Помилка]: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    """Визначає мову та коефіцієнт довіри за допомогою langdetect."""
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            langs = detect_langs(text)
            # Беремо ймовірність першого знайденого варіанту
            for item in langs:
                return str(item.prob)
            return "0.0"
        else:
            langs = detect_langs(text)
            lang_code = detect(text)
            prob = 0.0
            for item in langs:
                if item.lang == lang_code:
                    prob = item.prob
                    break
            return f"Мова: {lang_code}, Коефіцієнт довіри: {prob}"
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
    """Виводить таблицю мов і виконує переклад за допомогою deep_translator."""
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
                try:
                    translated_text = GoogleTranslator(source='auto', target=code).translate(text)
                    row += f" {translated_text}"
                except:
                    row += " [Помилка перекладу]"
            lines.append(row)
            
        result_str = "\n".join(lines)
        
        if out == "file":
            with open("languages_output_deeptr.txt", "w", encoding="utf-8") as f:
                f.write(result_str)
        else:
            print(result_str)
            
        return "Ok"
    except Exception as e:
        return f"[Помилка]: {e}"