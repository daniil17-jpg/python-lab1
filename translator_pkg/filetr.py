import importlib
import re
import asyncio

def main():
    # Читаємо конфігураційний файл config.txt
    try:
        with open("config.txt", "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f.readlines() if line.strip()]
        
        file_name = lines[0]
        target_lang = lines[1]
        module_name = lines[2]
        output_dest = lines[3]
        max_sentences = int(lines[4])
    except Exception as e:
        print(f"Помилка читання конфігурації: {e}")
        return

    # Імпортуємо вказаний модуль
    try:
        mod = importlib.import_module(module_name)
    except Exception as e:
        print(f"Помилка імпорту модуля: {e}")
        return

    # Читаємо текст із файлу
    try:
        with open(file_name, "r", encoding="utf-8") as f:
            content = f.read()
            
        file_size = len(content.encode('utf-8'))
        char_count = len(content)
        
        # Розбиваємо на речення
        sentences = [s.strip() for s in re.split(r'[.!?]+', content) if s.strip()]
        sentence_count = len(sentences)
        
        # Визначаємо мову
        if hasattr(mod, 'LangDetect'):
            if asyncio.iscoroutinefunction(mod.LangDetect):
                text_lang = asyncio.run(mod.LangDetect(content, "lang"))
            else:
                text_lang = mod.LangDetect(content, "lang")
        else:
            text_lang = "не визначено"

        print(f"Назва файлу з текстом: {file_name}")
        print(f"Розмір файлу: {file_size} байт")
        print(f"Кількість символів: {char_count}")
        print(f"Кількість речень: {sentence_count}")
        print(f"Мова тексту: {text_lang}")
        print("-" * 30)

    except Exception as e:
        print(f"Помилка читання файлу тексту: {e}")
        return

    # Перекладаємо речення до заданого ліміту
    translated_list = []
    counter = 0
    for s in sentences:
        if counter >= max_sentences:
            break
        try:
            if hasattr(mod, 'TransLate'):
                if asyncio.iscoroutinefunction(mod.TransLate):
                    res = asyncio.run(mod.TransLate(s, 'auto', target_lang))
                else:
                    res = mod.TransLate(s, 'auto', target_lang)
                translated_list.append(res)
            counter += 1
        except Exception as e:
            translated_list.append(f"[Помилка: {e}]")

    final_result = " ".join(translated_list)

    # Виведення результату згідно конфігурації
    if output_dest == "file":
        out_name = f"translated_{target_lang}.txt"
        with open(out_name, "w", encoding="utf-8") as f:
            f.write(final_result)
        print("Ok")
    else:
        print(f"Цільова мова перекладу: {target_lang}")
        print(f"Використаний модуль: {module_name}")
        print(f"Результат:\n{final_result}")
        print("Ok")

if __name__ == "__main__":
    main()