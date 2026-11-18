# Q2: Student Marks Analysis (no loops, no functions)

# 1. Create a list of five marks and convert it to a tuple
marks_list = [78, 35, 92, 40, 61]
marks_tuple = tuple(marks_list)

# 2. Display both collections and their data types
print("List  :", marks_list, "->", type(marks_list))
print("Tuple :", marks_tuple, "->", type(marks_tuple))

# 3. Highest and lowest marks using built-in functions
highest = max(marks_list)
lowest = min(marks_list)
print("Highest mark:", highest)
print("Lowest mark :", lowest)

# 4. Count students who scored at least 40
# Each comparison gives True (1) or False (0), so adding them gives the count
passed_count = ((marks_list[0] >= 40) + (marks_list[1] >= 40) +
                (marks_list[2] >= 40) + (marks_list[3] >= 40) +
                (marks_list[4] >= 40))
print("Students with at least 40 marks:", passed_count)

# 5. Check that all marks are within 0 to 100
# If the lowest is >= 0 and the highest is <= 100, every mark is in range
all_valid = lowest >= 0 and highest <= 100
print("All marks within 0-100:", all_valid)

# 6. Changing one element in the list and one in the tuple
marks_list[1] = 45
print("List after changing index 1 to 45:", marks_list)

# marks_tuple[1] = 45   # <- Uncommenting this line gives:
#                       # TypeError: 'tuple' object does not support item assignment

# Observation: A list is mutable, so its elements can be changed after creation
# (the list now holds 45 at index 1). A tuple is immutable, so assigning to one
# of its elements raises a TypeError. That is why the tuple line is commented
# out, so the program can run. The tuple still holds the original marks:
print("Tuple is unchanged:", marks_tuple)
