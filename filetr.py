import json
import os
import sys

def get_module(module_name):
    if module_name == "gtrans4":
        from Harkavyi import gtrans4_mod as mod
    elif module_name == "gtrans3":
        from Harkavyi import gtrans3_mod as mod
    elif module_name == "deeptr":
        from Harkavyi import deeptr_mod as mod
    else:
        raise ValueError("Невідомий модуль у конфігурації")
    return mod

def main():
    try:
        with open("config.json", "r", encoding="utf-8") as f:
            config = json.load(f)
    except Exception as e:
        print(f"Помилка конфігурації: {e}")
        return

    txt_file = config['text_file']
    if not os.path.exists(txt_file):
        print(f"Помилка: Файл {txt_file} не знайдено.")
        return

    file_size = os.path.getsize(txt_file)
    with open(txt_file, "r", encoding="utf-8") as f:
        content = f.read()
    
    sentences = [s.strip() for s in content.split('.') if s.strip()]
    
    print(f"Назва файлу: {txt_file}")
    print(f"Розмір файлу: {file_size} байт")
    print(f"Кількість символів: {len(content)}")
    print(f"Кількість речень: {len(sentences)}")

    from Harkavyi import gtrans4_mod
    print(f"Мова тексту: {gtrans4_mod.LangDetect(content, 'lang')}")
    print("-" * 30)

    limit = config.get('sentences_limit', len(sentences))
    text_to_translate = ". ".join(sentences[:limit]) + "."
    try:
        mod = get_module(config['module_to_use'])
        translated_text = mod.TransLate(text_to_translate, "auto", config['target_language'])
        if config['output'] == "screen":
            print(f"Мова перекладу: {config['target_language']}")
            print(f"Використаний модуль: {config['module_to_use']}")
            print(f"Переклад:\n{translated_text}")
        else:
            base_name = os.path.splitext(txt_file)[0]
            out_file = f"{base_name}_{config['target_language']}.txt"
            with open(out_file, "w", encoding="utf-8") as f:
                f.write(translated_text)
            print("Ok")

    except Exception as e:
        print(f"Помилка під час перекладу: {e}")

if __name__ == "__main__":
    main()