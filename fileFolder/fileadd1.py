import os
cwd = os.getcwd()
filename = "addfile1"
openmode = "a"
print("the current work path is:",cwd)
f = open(cwd+"\\"+filename,openmode)
f.write("add one line!\n")
f.close()