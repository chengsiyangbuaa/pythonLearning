f = open("..\\fileFolder1\\datafile.txt","w")
f.write("Hello world!\n")
f.write("write this line in another dir\n")
f.close()
#..\\两个点代表父文件夹
#D:\buaa\pythonLearning\fileFolder\    == .\\
#D:\buaa\pythonLearning\              == ..\\
#D:\buaa\pythonLearning\fileFolder1\\datafile.txt              == ..\\fileFolder1\\datafile.txt