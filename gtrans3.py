from Harkavyi.gtrans3_mod import TransLate, LangDetect, CodeLang, LanguageList

def main():
    print("модуль 2 (googletrans 3.1.0a0)\n")
    
    print("-Тест TransLate-")
    print(f"Переклад (uk -> en): {TransLate('Модуль для перевірки Docker-контейнеру', 'uk', 'en')}\n")
    
    print("-Тест LangDetect-")
    print(f"Код мови та confidence: {LangDetect('Hello my friend', 'all')}\n")
    
    print("-CodeLang-")
    print(f"Перевірка назви 'ukrainian': {CodeLang('ukrainian')}\n")
    
    print("-Тест LanguageList-")
    LanguageList("screen", "Світ")

if __name__ == "__main__":
    main()