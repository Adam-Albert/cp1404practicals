
from programming_language import ProgrammingLanguage

ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

print("{}\n{}\n{}".format(ruby, python, visual_basic))
programming_languages = [ruby, python, visual_basic]
print("the dynamically typed languages are:")
for language in programming_languages:
    if language.is_dynamic():
        print(language.name)
