from Harkavyi.deeptr_mod import TransLate, LangDetect, CodeLang, LanguageList

def main():
    print("модуль 3 (deep_translator + langdetect)\n")
    
    print("-Тест TransLate-")
    text_to_translate = "Перевірка третього модулю"
    print(f"Оригінал: {text_to_translate}")
    print(f"Переклад (uk -> en): {TransLate(text_to_translate, 'uk', 'en')}\n")
    
    print("-Тест LangDetect-")
    text_to_detect = "Hello my friend"
    print(f"Текст: {text_to_detect}")
    print(f"код мови та confidence: {LangDetect(text_to_detect, 'all')}")
    print(f"Код мови: {LangDetect(text_to_detect, 'lang')}\n")
    
    print("-Тест CodeLang-")
    print(f"Перевірка назви мови (Українська): {CodeLang('ukrainian')}")
    print(f"Перевірка коду мови (Німецька): {CodeLang('de')}\n")
    
    print("-Тест LanguageList-")
    print("переклад слова 'Дякую':")
    LanguageList("screen", "Дякую")

if __name__ == "__main__":
    main()