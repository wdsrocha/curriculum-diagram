# coding=utf8

import re

raw_curriculum = open("./curriculum.txt")
regex_course = r"^([A-Z]+\d+) - ([^\t\n]+)\t?([^\n]*)$"
regex_semester = r"^Série: (\d) - \1º PERÍODO$"
for line in raw_curriculum:
    matches = re.finditer(regex_course, line)
    for match in matches:
        print("Código: {}".format(match.group(1)))
        print("Nome: {}".format(match.group(2)))
        print("Pré-requesito(s): {}".format(match.group(3)))
        print()
