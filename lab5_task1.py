import re

UKRAINIAN_ALPHABET = "абвгґдеєжзиіїйклмнопрстуфхцчшщьюя"

def sort_key(word: str):
    cleaned_word = re.sub(r'[^\w\s]', '', word)
    if not cleaned_word:
        return (2, word)

    first_char = cleaned_word[0].lower()
    if first_char in UKRAINIAN_ALPHABET:
        return (0, cleaned_word.lower())
    else:
        return (1, cleaned_word.lower())

def sort_text(text: str) -> list:
    words = re.findall(r'\b[\w\'-]+\b', text)
    return sorted(words, key=sort_key)

if __name__ == "__main__":
    with open("text.txt", "r", encoding="utf-8") as f:
        content = f.read()

    print("=== Оригінальний текст ===")
    print(content)
    print("\n=== Відсортовані слова ===")
    print(sort_text(content))