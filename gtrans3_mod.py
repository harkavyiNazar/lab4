import sys
from googletrans import Translator, LANGUAGES

if sys.version_info >= (3, 13):
    print("Помилка: Модуль googletrans==3.1.0a0 не підтримується в Python 3.13.")
    sys.exit(1)

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        result = translator.translate(text, src=scr, dest=dest)
        return result.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        result = translator.detect(text)
        if set == "lang":
            return result.lang
        elif set == "confidence":
            return str(result.confidence)
        else:
            return f"Language: {result.lang}, Confidence: {result.confidence}"
    except Exception as e:
        return f"Error: {e}"

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in LANGUAGES:
        return LANGUAGES[lang].capitalize()
    for code, name in LANGUAGES.items():
        if name.lower() == lang:
            return code
    return "Error: Language not found"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        translator = Translator()
        lines = []
        header = f"{'N':<4} | {'Language':<20} | {'ISO-639 code':<15}" + (f" | {'Text'}" if text else "")
        lines.append(header)
        lines.append("-" * len(header))
        
        count = 1
        for code, name in LANGUAGES.items():
            row = f"{count:<4} | {name.capitalize():<20} | {code:<15}"
            if text:
                try:
                    res = translator.translate(text, dest=code)
                    row += f" | {res.text}"
                except Exception:
                    row += f" | Error"
            lines.append(row)
            count += 1
            
        output_str = "\n".join(lines)
        if out == "screen":
            print(output_str)
        elif out == "file":
            with open("language_list3.txt", "w", encoding="utf-8") as f:
                f.write(output_str)
        return "Ok"
    except Exception as e:
        return f"Error: {e}"