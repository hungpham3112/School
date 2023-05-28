from lib import *

print(
    """
##################################
########## Question 1 ############
##################################
"""
)


file = input("Read content from: ").strip()
print(read_content(file))


file = input("File need to check: ").strip()
char = input("Character: ")
print(
    f"""The number of line does not start with {char}: {num_line_without_char(file, char)}"""
)

print(
    """
##################################
########## Question 2 ############
##################################
"""
)


file = input("File: ").strip()
print(hash_display(file))


file = input("File: ").strip()
print(JTOI(file))
