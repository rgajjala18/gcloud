textfile = open("logs.txt")
lines = textfile.readlines()
i = 0
list = []
for line in reversed(lines):
    if "Face" in line:
        i +=1
        if i > 3:
            break
        list.append(line[line.find("Face"):len(line)])
print(list[2])
print(list[1])
print(list[0])