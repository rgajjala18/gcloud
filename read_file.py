textfile = open("logs.txt")
lines = textfile.readlines()
i = 0
for line in reversed(lines):
    if "Face" in line:
        i +=1
        if i > 3:
            break
        print(line[line.find("Face"):len(line)])