""" REMEMBER TO CLOSE FILES!!! """

# Open the file for reading
read_file = open("text.txt", "r")

# Use a second file handler to open the file for writing
write_file= open("text.txt", "w")
# Write to the file
write_file.write("Hello ")

# Close write_file
write_file.close()

#read from the file
print read_file.read()

# Close read_file
read_file.close()



# with ... as ...:    automatically closes file for you
with open("text.txt", "w") as file:
    file.write("Hello World!")

with open("text.txt", "r") as file:
    print file.read()

