filename = 'output.txt'

# Step 1: Take user input and write to the file (overwrite if it exists)
text_write = input("Enter text to write to the file: ")
file1 = open(filename, 'w')
file1.write(text_write + '\n')
file1.close()
print(f"Data successfully written to {filename}.")

# Step 2: Take additional input and append it to the same file
text_append = input("Enter additional text to append: ")
file1 = open(filename, 'a')
file1.write(text_append + '\n')
file1.close()
print("Data successfully appended.")

# Step 3: Read and display the final content of the file
try:
    file1 = open(filename, 'r')
    print(f"\nFinal content of {filename}:")
    print(file1.read())
    file1.close()
except FileNotFoundError:
    print(f"Error: The file '{filename}' was not found.")
