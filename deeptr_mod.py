from deep_translator import GoogleTranslator
from langdetect import detect, detect_langs

langs_dict = GoogleTranslator().get_supported_languages(as_dict=True)

def CodeLang(lang: str) -> str:
    lang = lang.lower()
    if lang in langs_dict.values():
        for name, code in langs_dict.items():
            if code == lang:
                return name.capitalize()
    if lang in langs_dict.keys():
        return langs_dict[lang]
    return "Error: Language not found"

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        src_code = CodeLang(scr) if len(scr) > 2 and scr != 'auto' else scr
        dest_code = CodeLang(dest) if len(dest) > 2 else dest
        
        translator = GoogleTranslator(source=src_code, target=dest_code)
        return translator.translate(text)
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        if set == "lang":
            return detect(text)
        elif set == "confidence":
            langs = detect_langs(text)
            return str(round(langs[0].prob, 2)) if langs else "0"
        else:
            langs = detect_langs(text)
            conf = str(round(langs[0].prob, 2)) if langs else "0"
            return f"Language: {detect(text)}, Confidence: {conf}"
    except Exception as e:
        return f"Error: {e}"

def LanguageList(out: str = "screen", text: str = "") -> str:
    try:
        lines = []
        header = f"{'N':<4} | {'Language':<20} | {'ISO-639 code':<15}" + (f" | {'Text'}" if text else "")
        lines.append(header)
        lines.append("-" * len(header))
        
        count = 1
        for name, code in langs_dict.items():
            row = f"{count:<4} | {name.capitalize():<20} | {code:<15}"
            if text:
                try:
                    res = GoogleTranslator(source='auto', target=code).translate(text)
                    row += f" | {res}"
                except Exception:
                    row += f" | Error"
            lines.append(row)
            count += 1
            
        output_str = "\n".join(lines)
        if out == "screen":
            print(output_str)
        elif out == "file":
            with open("language_list_deep.txt", "w", encoding="utf-8") as f:
                f.write(output_str)
        return "Ok"
    except Exception as e:
        return f"Error: {e}"