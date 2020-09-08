

#
# To Import your code from a different file,
# first you have to [pip install import_ipynb] in the ANACONDA Prompt
# and then add the import here, then Notebook will recognise your file
#
import samwise_tools

s_filein = "/"
b_show_info = True
s_fileout = ""
while s_filein != "x":
    if b_show_info:
        s_prompt = "(\"x\" - to exit)\n(\"=\" - use new name)\n(\"?\" - show/hide help):\n"
        s_promptb = ""
    else:
        s_prompt = ""
        s_promptb = "(\"?\",\"=\",\"x\")"
    s_filein = input("Enter File Name [format: name.xxx]" + s_promptb + ":\n"+s_prompt)
    if s_filein not in ("x", "?", ""):
        if s_filein == "=":
            s_filein = s_fileout
        s_fileout = samwise_tools.get_inc_file_ext(s_filein)
        if s_fileout[0] == "x":
            print(s_fileout[1:])
        else:
            print("\nNew Name[{0}]".format(s_fileout))
            if s_fileout[0] == "?":
                s_fileout = " "
            else:
                if b_show_info:
                    print("File Incremented by 1\n")
                s_period = s_filein.index(".")
                s_left_of_period = s_filein[:s_period]
            # print("{0}\n{1}\n".format(s_period, s_left_of_period))

                s_split = samwise_tools.get_str_left_num_right(s_left_of_period)
            # print (s_split)
                if b_show_info:
                    print("Left Part In : [{0}] \nRight Part In: [{1}]".format(s_split[0], s_split[1]))
                    print("New Name Out : [{0}]".format(s_fileout))
                    print("==========================")
    elif s_filein == "?":
        if b_show_info:
            b_show_info = False
        else:
            b_show_info = True


print("*** Ended ***")
