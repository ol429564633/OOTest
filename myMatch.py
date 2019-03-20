from sympy import *
from config import config
import random
import time


def match(strs, standard):
    pat_string = standard
    print(time.asctime(time.localtime(time.time())))
    print(standard)
    num1 = random.uniform(-1.5, 0.3)
    num2 = random.uniform(0.3, 1.5)
    x = Symbol("x")

    p = True
    newStrs = {}
    mark = {}
    for temp_str in strs:
        str1 = strs[temp_str].replace("^", "**")
        if str1.strip() == "WRONG FORMAT!":
            str1 = "8848*x"
            standard = "4424*x^2"
        print(temp_str)
        newStrs.update({temp_str: simplify(str1)})
        mark.update({temp_str: True})

    standard = standard.replace("^", "**")
    standard = simplify(standard)
    standard = diff(standard, x)
    standard_anses = [standard.evalf(subs={x: num1}), standard.evalf(subs={x: num2})]
    print(standard)

    for string in newStrs:
        temp_anses = [newStrs[string].evalf(subs={x: num1}), newStrs[string].evalf(subs={x: num2})]
        if temp_anses[0] != standard_anses[0] and temp_anses[1] != standard_anses[1]:
            mark.update({string: False})
            p = False
    if not p:
        print("\033[1;30;43mFAIL!\033[0m")
        file = open(config.diff_file, "a")
        file.write("---------------------\n")
        file.write("PatString:" + pat_string + "\n")
        file.write("Standard:" + str(standard) + " || ans:" + str(standard_anses) + "\n")
        for temp_str in newStrs:
            temp_anses = [newStrs[temp_str].evalf(subs={x: num1}), newStrs[temp_str].evalf(subs={x: num2})]
            file.write(temp_str + ":" + str(newStrs[temp_str]) + " || ans:" + str(temp_anses))
            if not mark[temp_str]:
                file.write(" FAIL!\n")
            else:
                file.write(" SUCCEED!\n")
        file.close()
