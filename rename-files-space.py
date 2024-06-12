import os

files = os.listdir("./content/papers/")
for file in files:
    s = file.split(" ")
    l = "-".join(s)
    print("========")
    print(file)
    print(l)
    os.rename(file, l)
