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
            item = re.findall(r"ITEM_\w*", evo.string)
            print(f"{s} via {item[0][4:]} \n" if item else f"{s} \n")
            f2.write(f"{s} via {item[0][5:].capitalize()} \n" if item else f"{s} \n")
        else:
            next = re.findall(r"\, SPECIES_.[A-z]*", evo.string)
            if next:
                nexts = f"{mon.capitalize()} -> "
                for i in next:
                    nextev = i.split("_")[1:]
                    allevs = " ".join(map(str, nextev))
                # for j in evo_items:
                #     nextitem = i.split("_")[1:]
                #     evoitem = " ".join(map(str, nextitem))
                evo_items = re.findall(r"ITEM_\w*", evo.string)

                if evo_items:
                    for i, j in zip(next, evo_items):
                        nextev = i.split("_")[1:]
                        allevs = " ".join(map(str, nextev))
                        nextitem = j.split("_")[1:]
                        evoitem = " ".join(map(str, nextitem))
                        nexts = nexts + allevs + " via " + evoitem
                else:
                    for i in next:
                        nextev = i.split("_")[1:]
                        allevs = " ".join(map(str, nextev))
                        nexts = nexts + allevs + " "

                print(f"{nexts} @ {lvl}\n")
                f2.write(f"{nexts} @ {lvl}\n")

            # print(f"{mon.capitalize()} -> {next} @ {lvl}")
            # f2.write(f"{mon.capitalize()} -> {next} @ {lvl} \n")
