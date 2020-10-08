response = input("Enter a temperature to convert(e.g. 74F, 75C):")

unit = response[-1]
digit = int(response[:-1])

if unit.upper() == "C":
    result = (digit * 9)//5 + 32
    new_unit = "F"

elif unit.upper() == "F":
    result = (digit - 32 * 5)//9
    new_unit = "C"
else:
    print("Invalid input, please follow the specified input format.")
    quit()

print("The converted temperature is:",result,new_unit)
