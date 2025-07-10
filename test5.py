with open("example.txt", "w") as file:
    file.write("This is the first line.\n")
with open("example.txt","r")as file:
    content = file.read()
words = content.split()
word_count = len(words)
print(f"Total number of words: {word_count}")