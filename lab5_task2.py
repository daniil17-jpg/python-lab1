import urllib.parse
import pyperclip

def decode_url(encoded_url: str) -> str:
    return urllib.parse.unquote(encoded_url)

if __name__ == "__main__":
    test_url = "https://uk.wikipedia.org/wiki/%D0%A8%D1%82%D1%83%D1%87%D0%BD%D0%B8%D0%B9_%D1%96%D0%BD%D1%82%D0%B5%D0%BB%D0%B5%D0%BA%D1%82"

    print("Закодоване посилання:")
    print(test_url)

    decoded = decode_url(test_url)
    print("\nДекодоване посилання:")
    print(decoded)

    pyperclip.copy(decoded)
    print("\n[Успіх] Посилання скопійовано в буфер обміну!")