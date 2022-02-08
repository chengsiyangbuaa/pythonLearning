import os
cwd = os.getcwd()
filename = "os_cwd_file"
openmode = "w"
print("the current work path is:",cwd)
f = open(cwd+"\\"+filename,openmode)
f.write("Hello world!\n")
f.write("use os.getcwd() to get the path to write file!\n")