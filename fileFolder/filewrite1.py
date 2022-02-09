#读写
f = open(".\\datafile.txt","w") # 写或创建文件。
f.write("Hello world!\n")
f.write("Write in current dir!\n")
print(type(f))
f.close() # 为什么要关掉，控制文件读写需要花费资源，
#D:\buaa\pythonLearning\fileFolder\
#绝对路径、相对路径
#.\\datafile.txt
