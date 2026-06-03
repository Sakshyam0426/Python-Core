# Control flow statements: if, elif, else, match-case, try / except

# if/elif/else = Conditional branching
# match-case = Pattern matching (Python's switch)
# try / except = Handle errors / control exception flow


# if statements

Temperature   = 35

if Temperature > 30:
    print("\nIt's hot outside.\n")

if Temperature > 20:
    print("\nIt's warm today.\n")

if Temperature == 35:
    print("\nTemperature is exactly 35°C.\n")





# if-else statement
y = 10
if y % 2 == 0:
    print(f"{y} is even \n")  
else:
    print(f"{y} is odd \n")





# if-elif-else statement
z = 15
if z < 10:
    print(f"{z} is less than 10")
elif z == 10:
    print(f"{z} is equal to 10")
else:
    print(f"{z} is greater than 10")




# match-case statement
day = "Sunday"

match day:
    case "Monday":
        print("\nStart of the Study week\n")
    case "Friday":
        print("\nEnd of the Study week\n")
    case "Saturday" | "Sunday":
        print("\nFun in Weekend\n")
    case default:                       # default case
        print("\nBoring Day\n")





 # try / except / finally statement
try:
    num = int(input("Enter a Number"))
    x = 100 / num
    print(f"x: {x}")
except ValueError:
    print("Error handled!")
finally:
    print("Program still running!")




