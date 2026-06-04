# Creating a fuction using the 'def' keyword
def main():
    print("\nHELLO PYTHON")

main()                          # calling the function



# Function with Parameters
def Good_Person(name):
    print(f"{name}")

Good_Person("\nSakshyam Paudel \n")



# Any Number of Arguments
def total(*numbers):
    return sum(numbers)

print(total(1, 3, 5, 1))           
