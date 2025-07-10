with open("example.txt", "w") as file:
    file.write("This is the first line.\n")
with open("example.txt", "a") as file:
    file.write("This is the second line.\n")
with open("example.txt", "r") as file:
    contents = file.read()
    print("File Contents:\n")
    print(contents)