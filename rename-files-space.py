import os

path = "./content/papers/"
files = os.listdir(path)
for file in files:
    s = file.split(" ")
    if len(s) == 1:
        continue
    s = [i.strip(":") for i in s]
    l = "-".join(s)
    print("========")
    print(file)
    print(l)
    os.rename(path + file, path + l)
