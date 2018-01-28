# coding=utf8

from course import Course
import re

if __name__ == '__main__':
    semesters = [[]]
    raw_curriculum = open("./curriculum.txt")
    regex_course = r"^([A-Z]+\d+) - ([^\t\n]+)\t?([^\n]*)\t?([^\n]*)$"
    for line in raw_curriculum:
        m = re.match(regex_course, line)
        if m:
            semesters[-1].append(Course(
                m[1], m[2], m[3], m[4]
            ))
            print(semesters[-1][-1].displayData())
            print()
        elif semesters[-1] != []:
            semesters.append([])
