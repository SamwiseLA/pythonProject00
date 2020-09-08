# Code look at a List, changes +++ to \n - Done because Read files treat /n as a new row.

l_line = ["1 Hello+++  Lets do lunch", "\n", "2 Line Data", "\n", "3 Line Data", "\n", "4 line+++  the+++  end"]
last_line = -1

test_list = []
for i in range(len(l_line)):
    test_list.append("")
    checkline = -1
    for line in l_line:
        checkline += 1
        if checkline > last_line:
            last_line = checkline
            if line != "\n":
                examined_for_new_line = line.replace("+++", "\n")
                test_list[i] += examined_for_new_line
                break
            elif line == "\n":
                break

for ln in test_list:
    print(f"{ln}")
