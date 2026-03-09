from Harkavyi.gtrans4_mod import TransLate, LangDetect, CodeLang, LanguageList

def main():
    print("модуль 1 (googletrans 4.0.2)\n")
    
    print("-TransLate-")
    text_to_translate = "Я студент Факультету інформаційних технологій"
    print(f"Оригінал: {text_to_translate}")
    print(f"Переклад (uk -> en): {TransLate(text_to_translate, 'uk', 'en')}\n")
    
    print("-LangDetect-")
    text_to_detect = "Bonjour tout le monde"
    print(f"Текст: {text_to_detect}")
    print(f"Мова : {LangDetect(text_to_detect, 'all')}")
    print(f"Код мови : {LangDetect(text_to_detect, 'lang')}\n")
    
    print("-CodeLang-")
    print(f"перевірка коду української мови: {CodeLang('ukrainian')}")
    print(f"перевірка назви мови (французька): {CodeLang('fr')}\n")
    
    print("-LanguageList-")
    print("Таблиця мов:")
    LanguageList("screen", "Привіт")
if __name__ == "__main__":
    main()