# List data type in python

# Declaring and initializing list variables
fruits = ["apple", "banana", "mango",]
more_fruits = ["grapes", "persimmon", "melon"]


print(f"\n\nList Data Manipulation")
print(f"\nOriginal list: {fruits}")

# List methods for list manipulation
# append
# remove
# extend
# insert
# count
# index
# clear
# empty
# reversed


# 1. Adding new data to the end of the list (Append)
fruits.append("apple")
print(f"\nList after appending data: {fruits}")


# 2. Removing data from the list using values (Remove)
fruits.remove("banana")
print(f"\nList after removing data: {fruits}")



# 3.  Joining two lists together (Extend)
fruits.extend(more_fruits)
print(f"\nAfter joining another list to fruits: {fruits}")



# 4.Inserting new data into a specific position in the list (Insert)
fruits.insert(2, "lemon")
print(f"\nInserting new data to index 2 of the list: {fruits}")



# 5. Counting the number of times a specific value appears in a list (Count)
num_of_apples = fruits.count("apple")
print(f"\nNumber of times 'apple' appears in the list: {num_of_apples}")



# 6. Removing list data with index value
index_of_grapes = fruits.index("grapes")
fruits.pop(index_of_grapes)
print(f"\nRemoving data from list with their positional(index) value: {fruits}")
numbers = [2, 7, 1, 4, 3, 9, 5]
print(f"\n\nOriginal number list: {numbers}")



# 7.  Reversing the order of the list
reversed_numbers = numbers.reverse()
print(f"\nNumbers list, reversed: {reversed_numbers}")


# 8. Nested Lists (2D List)

print("\nNested Lists")
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print("Matrix:", matrix)
print("Row 1:", matrix[0])          # [1, 2, 3]
print("Element [1][2]:", matrix[1][2])  # 6





# 9. Sorting the list in ascending order
numbers.sort()
print(f"\nSorted Numbers list: {numbers}") # Sorts in ascending order by default



# 10. Sorting the list in descending order
numbers.sort(reverse=True)
print(f"\nSorted Numbers list: {numbers}")




# 11. Emptying lists
fruits.clear()
numbers.clear()
print(f"\n\nClearing the entire lists:")
print(f"\nFruits list: {fruits}")
print(f"\nNumbers list: {numbers}")


