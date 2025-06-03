#############
# Lesson 2: INT
#############

# Interactive mode
" Just type python3 in terminal. executes lines of codes written after >>>"



# INT
# these will be str values, thus we need to convert them to int
' x = int(input("What is x? ")) '
' y = int(input("What is y? ")) '

#now print will add the int values.
' print(x + y) '



# FLOAT - decimal point
' x = float(input("What is x? ")) '
' y = float(input("What is y? ")) '

#now print will add the int values.
#round - round(number[, ndigits])
#   ndigits: rounds to the number of decimals

' z = round(x + y) '
' print(z) '

#Format with , (for 1,000)
' print(f"{z:,}") '


# Division /
x = float(input("What is x? "))
y = float(input("What is y? "))

# round to 2 digits
z = round(x / y , 2)
print(z)

#another way to specify number of digits to print:
print(f"{z:.3f}")
