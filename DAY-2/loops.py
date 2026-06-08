# for loop = loop over a sequence
# While loop = loop while condition is true
# Break = stop the loop immediately
# Continue = skip current step, keep going
# Range() = generate numbers
# enumerate() = get index + value together


# for loop
for star in range(6):                    # loop from 0 to 5
    print(f"{star}", end=" ")
print("\n")


for planet in range(2, 20, 3):           # loop from 2 to 19 with a step of 3 (2, 5, 8, 11, 14, 17)
    print(f"{planet}", end=" ")
print("\n")                              # prints a newline after the loop is done


# for loop in strings
for letter in "SAKSHYAM":
    print(f"{letter}", end=" ")          # prints each character in the string "Galaxy"
print("\n")


# for loop with break
for star in range(15):                   # loop from 0 to 14
    if star == 2:
        break                            # exit the loop when star is 7
    print(f"{star}", end=" ")
print("\n")


# for loop with continue
for star in range(30):                   # loop from 0 to 14
    if star % 3 == 0:
        continue                         # skip multiples of 3
    print(f"{star}", end=" ")            # prints only non-multiples of 3
print("\n")


# while loop
moon = 0
while moon < 50:                          # loop until moon is less than 8
    print(f"{moon}", end=" ")
    moon += 8                          # *important* to avoid infinite loop
print("\n")


# while loop with break
variable = 0
while variable < 20:                        # loop until comet is less than 20
    if variable == 9:
        break                            # exit the loop when comet is 9
    print(f"{variable}", end=" ")
    variable += 1
print("\n")


# while loop with continue
comet = 0
while comet < 20:                        # loop until comet is less than 20
    if comet % 3 == 0:
        comet += 1
        continue                         # skip multiples of 3
    print(f"{comet}", end=" ")           # prints only non-multiples of 3
    comet += 1
print("\n")
