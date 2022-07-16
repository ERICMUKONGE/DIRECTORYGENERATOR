import os

for path, dirs, files in os.walk("C:/Users/e/Downloads"):
    print("The current folder is : " + path)
    for dir in dirs:
        print("Sufolder of : " +" : " + path + dir)
    for file in files:
        print("Folder Inside : " + " : " + path + file)    