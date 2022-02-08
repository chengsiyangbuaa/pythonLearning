#标准输入流
import sys

f = open("input.txt","w")
f.write("xiao_qie_zi\n")
f.write("4396\n")
f.close()

# 重定向
fIn = open("input.txt","r")
sys.stdin = fIn #默认的标准输入流是从键盘输入，这里将标准输入流改为fIn文件流输入
fOut = open("output.txt","w")
sys.stdout = fOut #同上
fError = open("error.txt","w")
sys.stderr = fError #同上

sname = input()
damage = input()

print("{name} 's damage is {dam}".format(name = sname,dam = damage))
fIn.close()
fOut.close()
raise Exception("Raise an execption!")
fError.close()