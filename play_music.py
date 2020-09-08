from playsound import playsound

# s_mfile = "Groove40.mp3"

# s_mfile = "/Users/samwiseaaron/Desktop/Groove40x.mp3"
# s_mfile = "/Users/samwiseaaron/Desktop/Groove 40x.mp3"
# s_mfile = "/Users/samwiseaaron/Desktop/Groove 40x.mp3"
s_mfile = "/Users/samwiseaaron/Google\ Drive/A\ -\ Classes/Production/TripleThreatArtist/Lab\ Work/100\ Grooves/TTA\ -\ Groove\ 41\ -\ Do\ It\ Now\ -\ Logic\ on\ Love\ Seat\ -\ 2020-08-013.mp3"

s_mfile_in = s_mfile
s_mfile_run = s_mfile_in

print("Check for \" \"...")
try:
    i_pos = s_mfile_run.index(" ")
    print("Space found @ pos: " + str(i_pos) + " will replace with \"%20\"")
    s_mfile_run = s_mfile_run.replace(" ", "%20")
except ValueError:
    print("No Space found")

print("----------------------")

print("Check for \"\\\\\"...")
try:
    i_pos = s_mfile_run.index("\\")
    print("\"\\\\\" found @ pos: " + str(i_pos)+ " will replace with \"\"")
    s_mfile_run = s_mfile_run.replace("\\", "")
except ValueError:
    print("No Escape \"\\\\\" found")
print("----------------------")

print("File In :\n[" + s_mfile_in + "]")
print("File Run:\n[" + s_mfile_run + "]")

playsound(s_mfile_run)

print("Done!")
