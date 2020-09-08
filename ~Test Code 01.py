# Use Existing PYTHON files
import samwise_tools

print("=========== Start ===================")

file = input("File Name to be incremented,\nmust have .??? format: ")
fileNew = "?"
while fileNew[0] == "?":
    fileNew = samwise_tools.get_inc_file_ext(file)
    if fileNew[0] != "?":
        print("\nThe Incremendted File Name is: {0}".format(fileNew))
    else:
        print(fileNew[1:])
        file = input("File Name to be incremented, must have .??? format")
exit()

