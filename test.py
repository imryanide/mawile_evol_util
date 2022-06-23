import re

f = open("evolution.h")

print("file opened")
f2 = open("output.txt", "w")
for line in f:
    line = line.lstrip()
    evo = re.search(r"^\[SPECIES_*[A-Z]*", line)
    if evo:
        # Pokemon Name
        mon = re.findall(r"^\[SPECIES_*.*\]", line)[0][9:-1]
        # Pokemon level
        lvl = re.findall(r"([0-9][0-9]|[0-9])", evo.string)
        if lvl:
            lvl = lvl[0]
        else:
            lvl = "Final Evolution"
        # Pokemon Next Evolution
        megas = re.findall(r"SPECIES_MEGA_[A-z]*", evo.string)
        if megas:
            s = f"{mon.capitalize()} ->  "
            for i in megas:
                megaevo = i.split("_")[1:]
                mgs = " ".join(map(str, megaevo))
                s = s + mgs + " "
            print(f"{s} via Stone")
            f2.write(f"{s} via Stone \n")
        else:
            next = re.findall(r"\, SPECIES_.[A-z]*", evo.string)
            if next:
                nexts = f"{mon.capitalize()} -> "
                for i in next:
                    nextev = i.split("_")[1:]
                    allevs = " ".join(map(str, nextev))
                    nexts = nexts + allevs + " "
                print(f"{nexts} @ {lvl}\n")
                f2.write(f"{nexts} @ {lvl}\n")
            # print(f"{mon.capitalize()} -> {next} @ {lvl}")
            # f2.write(f"{mon.capitalize()} -> {next} @ {lvl} \n")
