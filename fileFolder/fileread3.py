import os
cwd = os.getcwd()
filename = "os_cwd_file"
openmode = "r"
print("the current work path is:",cwd)
f = open(cwd+"\\"+filename,openmode)
sLine1 = f.readline()
sLine2 = f.readline()
print(sLine1,sLine2)
f.close()