from fileinput import filename
import os
path = "..\\dataresourse"
files_name = os.listdir(path) # 获取path文件夹中的所有子文件名列表
file_value_dic = {}
print(type(file_value_dic))
print(files_name)
filemode = "r"
for sname in files_name:
    f = open(path+"\\"+sname,filemode)
    sline = f.readline()
    file_value_dic[sname] = sline
    f.close()

for file_name,file_value in file_value_dic.items():
    print("file:","\t",file_name,"\tvalue is:",file_value)
