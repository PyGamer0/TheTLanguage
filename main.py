# Super simple transplied language
import sys

file = sys.argv[1]
f = open(file, encoding='utf-8')
code = f.readlines()
f.close()
transplied = ""

for line in code:
    line = line.replace("def", "_def")
    line = line.replace("fn", "def")
    line = line.replace("return", "_return")
    line = line.replace("ret", "return")

    stripped = line.strip()
    if (stripped.startswith("if") or stripped.startswith("def") or stripped.startswith("class") or stripped.startswith("for") or stripped.startswith("elif") or stripped.startswith("else")):
        line = line[:-1] + ':\n'

    transplied += line

out = open(file + '.py', 'w+')
out.write(transplied)
out.close()
