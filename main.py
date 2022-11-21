'''
1-Crear una funcion que pase de entero > 0 y < 4000 a romano

2-Cualquier otra entrada debe dar error

Casos de prueba

a) 1994 -> MCMXCIV
b) 4000->RomanNumberError("el valor debe ser menor de 4000")
c)"unacadena" -> RomanNumberErro("debe ser un entero")
d)0-> RomanNumberError("el valor debe ser mayor a cero")
e)-3 ->RomanNumberError("el valor debe ser mayor de cero")
f)4.5 -> RomanNumberError("Debe ser un entero")
'''

# Function to ask the user to enter a valid number
def askCorrectNumber(message):
    number = 0
    while number == 0:
        try:
            value = input(message)
            number = int(value)
        except ValueError:
            number = 0
        if number > 0 and number < 4000:
            return value
        else:
            print ('The given value is not valid, it should be a positive integer number, you need to try again.')
            number = 0

def arabicToRomanNumber(arabicNumber):
    # Dictionary variable to include the equivalence between arabic and roman numbers
    arabicToRomanNumberEquivalence = { 1000:'M', 500:'D', 100:'C', 50:'L', 10:'X', 5:'V', 1:'I'}

    romanNumber = ""

    if arabicNumber == 0:
        romanNumber = ""
        return romanNumber

    for arabicKey, romanValue in arabicToRomanNumberEquivalence.items():
        if arabicNumber == arabicKey:
            romanNumber = romanValue
            return romanNumber
            break
        elif arabicNumber > arabicKey:
            if romanValue == "I" or romanValue == "X" or romanValue == "C" or romanValue == "M":
                if arabicKey * 2 == arabicNumber:
                    romanNumber = romanValue + romanValue
                    return romanNumber
                    break
                elif arabicKey * 3 == arabicNumber:
                    romanNumber = romanValue + romanValue + romanValue
                    return romanNumber
                    break
                else:
                    romanNumber = romanValue + arabicToRomanNumberEquivalence[arabicKey * 5]
                    return romanNumber
                    break
            else:
                if arabicKey + 1 * arabicKey/5 == arabicNumber:
                    romanNumber = romanValue + arabicToRomanNumberEquivalence[arabicKey / 5]
                    return romanNumber
                    break                    
                elif arabicKey + 2 * arabicKey/5 == arabicNumber:
                    romanNumber = romanValue + arabicToRomanNumberEquivalence[arabicKey / 5] + arabicToRomanNumberEquivalence[arabicKey / 5]
                    return romanNumber
                    break
                elif arabicKey + 3 * arabicKey/5 == arabicNumber:
                    romanNumber = romanValue + arabicToRomanNumberEquivalence[arabicKey / 5] + arabicToRomanNumberEquivalence[arabicKey / 5] + arabicToRomanNumberEquivalence[arabicKey / 5]
                    return romanNumber
                    break
                else:
                    romanNumber = arabicToRomanNumberEquivalence[arabicKey / 5] + arabicToRomanNumberEquivalence[arabicKey * 2]
                    return romanNumber
                    break

# Ask for number
number = askCorrectNumber("Write the number you want to transform: ")

# Transform given number into a list
digits = list(number)

# Add the number of zeros required depending if is units, tens, hundreds or thousands
for position in range(len(digits)):
    zerosToAdd = len(digits[position:])
    digits[position] = digits[position].ljust(zerosToAdd, "0")

# Convert each unit of the given number into a roman numeral with the function arabicToRomanNumber
# Creates a string that concatenates the tranformation to roman of each unit
romanNumber = ""

for digit in digits:
    arabicNumber = int(digit)
    romanNumber = romanNumber + arabicToRomanNumber(arabicNumber)

print(romanNumber)


