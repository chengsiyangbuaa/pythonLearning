import os
cwd = os.getcwd()#获得当前路径的绝对路径
filename = "os_cwd_file.txt"
openmode = "w"
print("the current work path is:",cwd)
print(cwd+"\\"+filename)
f = open(cwd+"\\"+filename,openmode)
f.write("Hello world!\n")
f.write("use os.getcwd() to get the path to write file!\n")