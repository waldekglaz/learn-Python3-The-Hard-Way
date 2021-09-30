from sys import argv
# takes arguments from the console
script, filename = argv
# open file and retun a corresponding file object
txt = open(filename)

print(f"Here's your file {filename}:")
# Read the file object
print(txt.read())
txt.close()

# print("Type the filename again:")
# file_again = input(">")

# txt_again = open(file_again)

# print(txt_again.read())
