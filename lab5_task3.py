import json

data = {
    "Дробязко": ["Даніїл", "Дмитрович", 2007],
    "Шевченко": ["Тарас", "Григорович", 1814],
    "Франко": ["Іван", "Якович", 1856],
    "Українка": ["Леся", "Петрівна", 1871],
    "Костенко": ["Ліна", "Василівна", 1930],
    "Сковорода": ["Григорій", "Савич", 1722],
    "Котляревський": ["Іван", "Петрович", 1769],
    "Нечуй-Левицький": ["Іван", "Семенович", 1838],
    "Стус": ["Василь", "Семенович", 1938],
    "Симоненко": ["Василь", "Андрійович", 1935]
}

def save_to_json(filename: str, payload: dict):
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(payload, f, ensure_ascii=False, indent=4)

def read_from_json(filename: str) -> dict:
    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)

if __name__ == "__main__":
    json_file = "students.json"

    save_to_json(json_file, data)
    print(f"Дані збережено у {json_file}")

    loaded_data = read_from_json(json_file)
    print("\n=== Прочитані дані з JSON ===")
    for surname, info in loaded_data.items():
        print(f"{surname}: {info[0]} {info[1]}, рік народження: {info[2]}")