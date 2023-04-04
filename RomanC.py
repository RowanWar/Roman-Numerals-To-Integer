def romanToInt():
    romanInput = str(input("""
Please input your roman numeral string:
I      =       1
V      =       5
X      =       10
L      =       50
C      =       100
D      =       500
M      =       1000

Input: """))
    
    conversionDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Handles subtraction when these characters are together
    outlierNumeralDict = {'IV': -2, 'IX': -2, 'XL': -20, 'XC': -20, 'CD': -200, 'CM': -200}


    convertedNumerals = int()
    # Stores the prev value to compare against for niche edge cases i.e. IV = 4, not 6 
    prevItem = ''
    
    # Gets the index of each item via len() and the value in the 2nd parameter
    for item in romanInput: 
        
        if item in conversionDict:
            outlier = prevItem + item

            # Subtracts the appropriate amount in the event of a niche case such as X + L being 60 individually, but 40 when together 
            if outlier in outlierNumeralDict:
                
                print('Outlier detected: ' + str(outlier) + ' - Subtracting...')
                convertedNumerals += (outlierNumeralDict.get(outlier))

            
            convertedNumerals += (conversionDict.get(item)) # Gets the key specified and appends it to a string
            prevItem += item


        else:
            print('"' + item + '" is not a valid roman numeral!')
            exit()

            
    print('\n   Conversion of String:' + ' "' + romanInput + '" = ' + str(convertedNumerals))
 

romanToInt()
