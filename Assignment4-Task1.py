filename = 'myfile.txt'

# Create or overwrite the file with content
file1 = open(filename, 'w')
file1.write("Reading file content:\n")
file1.write("Line 1: This is a sample text file.\n")
file1.write("Line 2: It contains multiple lines.\n")
file1.close()

# Read and display content with error handling
try:
    file1 = open(filename, 'r')
    content = file1.read()
    print(content)
    file1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
