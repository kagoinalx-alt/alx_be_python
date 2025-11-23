# Pattern Drawing with Nested Loops

# Step 1: Prompt the user for the size of the pattern
pattern_size = int(input("Enter the size of the pattern: "))

# Step 2: Initialize row counter
row = 0

# Step 3: Use a while loop to handle rows
while row < pattern_size:
    # Step 4: Use a for loop to print asterisks for each column
    for col in range(pattern_size):
        print("*", end="")  # print stars on the same line

    print()  # move to the next line after each row
    row += 1  # increment the row counter
