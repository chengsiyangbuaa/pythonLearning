with open("names.txt","r") as f:
    while True:
        char = f.read(1)
        if not char:
            break
        print(char,end=",")
print("\n**************************************************")
with open("names.txt","r") as f:
    for x in f.readlines():
        print(x,end="")
print("\n**************************************************")
with open("names.txt","r") as f:
    while True:
        line = f.readline()
        if not line:
            break
        print(line,end="")

print("\n**************************************************")
with open("names.txt","r") as f:
    for line in f:
        print(line,end="")
print("\n**************************************************")
lines = list(open("names.txt","r"))
for line in lines:
        print(line,end="")