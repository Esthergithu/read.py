with open("input.txt", "r") as file:
    data = file.read()
print("Contents of input.txt:")
print(data)

#writing a modified version of the data to a new file
with open("output.txt", "w") as file:
    file.write(data)
print("Data has been written to output.txt")

#asking the user for a file name
file_name = input("Enter the name of the file to read: ")
try:
    with open(file_name, "r") as file:
        data = file.read()
    print(f"Contents of {file_name}:")
    print(data)
finally:
    print("File operation completed.")