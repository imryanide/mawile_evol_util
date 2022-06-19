import re

f = open("test2.txt")

print("file opened")

for line in f:
    line = line.lstrip()
    evo = re.search(r"^\[SPECIES_*[A-Z]*", line)
    if evo:
        # Pokemon Name
        mon = re.findall(r"^\[SPECIES_*[A-Z]*", line)[0][9:]
        # Pokemon level
        lvl = re.findall(r"[0-9][0-9]", evo.string)
        if lvl:
            lvl = lvl[0]
        else:
            lvl = "Final Evolution"
        # Pokemon Next Evolution
        next = re.findall(r"\, SPECIES.*\}\,$", evo.string)[0][10:-3]

        print(f"{mon.capitalize()} -> {next.capitalize()} @ {lvl}")
