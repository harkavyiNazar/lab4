import asyncio
import sys
from googletrans import Translator, LANGUAGES

if sys.platform == 'win32':
    asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())

def TransLate(text: str, scr: str, dest: str) -> str:
    try:
        translator = Translator()
        result = asyncio.run(translator.translate(text, src=scr, dest=dest))
        return result.text
    except Exception as e:
        return f"Error: {e}"

def LangDetect(text: str, set: str = "all") -> str:
    try:
        translator = Translator()
        result = asyncio.run(translator.detect(text))
        
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
        lines = []
        if text:
            header = f"{'N':<4} | {'Language':<20} | {'ISO-639 code':<15} | {'Text'}"
        else:
            header = f"{'N':<4} | {'Language':<20} | {'ISO-639 code':<15}"
            
        lines.append(header)
        lines.append("-" * len(header))
        async def get_all_translations(txt):
            async with Translator() as client:
                tasks = []
                codes = list(LANGUAGES.keys())
                for code in codes:
                    tasks.append(client.translate(txt, dest=code))
                return await asyncio.gather(*tasks, return_exceptions=True)

        translations = []
        if text:
            results = asyncio.run(get_all_translations(text))
            for res in results:
                if isinstance(res, Exception):
                    translations.append("Error")
                else:
                    translations.append(res.text)

        count = 1
        for i, (code, name) in enumerate(LANGUAGES.items()):
            row = f"{count:<4} | {name.capitalize():<20} | {code:<15}"
            if text:
                row += f" | {translations[i]}"
            lines.append(row)
            count += 1
            
        output_str = "\n".join(lines)
        
        if out == "screen":
            print(output_str)
        elif out == "file":
            with open("language_list.txt", "w", encoding="utf-8") as f:
                f.write(output_str)
        return "Ok"
    except Exception as e:
        return f"Error: {e}"