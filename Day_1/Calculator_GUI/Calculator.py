def addition(x,y):
    total = float(x) + float(y) # Store sum of x and y in "total"
    return (str(total)) # Return the amount of total

def subtraction(x,y):
    total = float(x) - float(y) # Store sum of x and y in "total"
    return (str(total)) # Return the amount of total

def multiplication(x,y):
    i = 0 # total
    ii = 0 # Counter
    while int(ii) < int(y): # Loops ii until it is equal to y ( the amount of groups x is being put into)
        i += int(x) # i = x(input) + i(0). It counts the amount of times the loop is run
        ii += 1 # ii = ii(0) + 1 ; ii = 1 (ii will be the total returned)
        #if ii == y: # if ( and when) the value of i is equal to y
    return (str(float(i))) # return i (the total)

def mudulo(x,y):
     i = 0
     ii = 0

def division(dividend,divisor):
    dividend = float(dividend)
    divisor = float(divisor)
    if dividend < 0 and divisor < 0:
        sign = 1
    elif dividend < 0 and divisor > 0:
        sign = -1
    elif dividend > 0 and divisor < 0:
        sign = -1
    else:
        sign = 1
    dividend = abs(dividend)
    divisor = abs(divisor)
    quotient = 0
    while divisor <= dividend:
        dividend -= divisor
        quotient += 1
    return sign * (quotient)


def base2_to_base10(base_2):
    [num_bef_dec,num_after_dec] = base_2.split('.')
    output = 0
    output_1 = 0
    count = 0
    count_2 = -1
    for i in num_bef_dec:
        if i == '1':
            i = 2 ** count
            print(i)
            output += i
        count += 1
    for i in num_after_dec:
        if i == '1':
            i = 2 ** count_2
            print(i)
            output_1 += i
        count_2 -= 1
    output_1 = str(output_1)
    output_1 = output_1.replace(output_1[0],'')
    return (str(output) + str(output_1))

def base2_to_base8 (base_2):
     [num_bef_dec, num_after_dec] = base_2.split(".")
     print (num_bef_dec)
     print (num_after_dec)
     output = ""
     output_1 = ""
     count = 0
     side_a = len(num_bef_dec)
     print (side_a)
     side_b = len(num_after_dec)
     print (side_b)

     if side_a % 3 == 1:
         num_bef_dec = num_bef_dec[::-1] + "00"
         num_bef_dec = num_bef_dec[::-1]
         print (num_bef_dec)
     elif side_a % 3 == 2:
         num_bef_dec = num_bef_dec[::-1] + "0"
         num_bef_dec = num_bef_dec[::-1]
     if side_b % 3 == 1:
        num_after_dec = num_after_dec + "00"
     elif side_b % 3 == 2:
        num_after_dec = num_after_dec + "0"

     for index in range(0, side_a, 3):
         cur_group = num_bef_dec[index:index+3]

         if cur_group == "000":
             output = output + "0"
         elif cur_group == "001":
             output = output + "1"
         elif cur_group == "010":
             output = output + "2"
         elif cur_group == "011":
             output = output + "3"
         elif cur_group == "100":
             output = output + "4"
         elif cur_group == "101":
             output = output + "5"
         elif cur_group == "110":
             output = output + "6"
         elif cur_group == "111":
             output = output + "7"

     for index in range(0,side_b, 3):
          cur_group = num_after_dec[index: index + 3]

          if cur_group == "000":
             output_1 = output_1 + "0"
          elif cur_group == "001":
             output_1 == output_1 + "1"
          elif cur_group == "010":
             output_1 = output_1 + "2"
          elif cur_group == "011":
             output_1 = output_1 + "3"
          elif cur_group == "100":
             output_1 = output_1 + "4"
          elif cur_group == "101":
             output_1 = output_1 + "5"
          elif cur_group == "110":
             output_1 = output_1 + "6"
          elif cur_group == "111":
             output_1 = output_1 + "7"
     print (output + "." + output_1)

def base2_to_base6 (base_2):
    [num_bef_dec, num_after_dec] = base_2.split(".")
    print (num_bef_dec)
    print (num_after_dec)
    output = ""
    output_1 = ""
    count = 0
    side_a = len(num_bef_dec)
    print (side_a)
    side_b = len(num_after_dec)
    print (side_b)

    if side_a % 4 == 1:
        num_bef_dec = num_bef_dec[::-1] + "000"
        num_bef_dec = num_bef_dec[::-1]
        print (num_bef_dec)
    elif side_a % 4 == 2:
        num_bef_dec = num_bef_dec[::-1] + "00"
        num_bef_dec = num_bef_dec[::-1]
    elif side_a % 4 == 3:
        num_bef_dec = num_bef_dec[::-1] + "0"
        num_bef_dec = num_bef_dec[::-1]

    if side_b % 4 == 1:
        num_after_dec = num_after_dec + "000"

    elif side_b % 4 == 2:
        num_after_dec = num_after_dec + "00"

    elif side_b % 4 == 3:
        num_after_dec = num_after_dec + "0"


    for index in range(0, side_a, 4):
        cur_group = num_bef_dec[index:index+4]

        if cur_group == "0000":
            output = output + "0"
        elif cur_group == "0001":
            output = output + "1"
        elif cur_group == "0010":
            output = output + "2"
        elif cur_group == "0011":
            output = output + "3"
        elif cur_group == "0100":
            output = output + "4"
        elif cur_group == "0101":
            output = output + "5"
        elif cur_group == "0110":
            output = output + "6"
        elif cur_group == "0111":
            output = output + "7"
        elif cur_group == "1000":
            output =output + "8"
        elif cur_group == "1001":
            output = ouput + "9"
        elif cur_group == "1010":
            output = output + "A"
        elif cur_group == "1011":
            output = output + "B"
        elif cur_group == "1100":
            output = output + "C"
        elif cur_group == "1101":
            output = output + "D"
        elif cur_group == "1110":
            output = output + "E"
        elif cur_group == "1111":
            output = output + 'F'

        for index in range(0, side_b, 4):
            cur_group = num_after_dec[index:index+4]

        if cur_group == "0000":
            output_1 = output_1 + "0"
        elif cur_group == "0001":
            output_1 = output_1 + "1"
        elif cur_group == "0010":
            output_1 = output_1 + "2"
        elif cur_group == "0011":
            output_1 = output_1 + "3"
        elif cur_group == "0100":
            output_1 = output_1 + "4"
        elif cur_group == "0101":
            output_1 = output_1 + "5"
        elif cur_group == "0110":
            output_1 = output_1 + "6"
        elif cur_group == "0111":
            output_1 = output_1 + "7"
        elif cur_group == "1000":
            output_1 =output_1 + "8"
        elif cur_group == "1001":
            output_1 = output_1 + "9"
        elif cur_group == "1010":
            output_1 = output_1 + "A"
        elif cur_group == "1011":
            output_1 = output_1 + "B"
        elif cur_group == "1100":
            output_1 = output_1 + "C"
        elif cur_group == "1101":
            output_1 = output_1 + "D"
        elif cur_group == "1110":
            output_1 = output_1 + "E"
        elif cur_group == "1111":
            output_1 = output_1 + 'F'

    print (output + "." + output_1)




def Choice():
    Question = input("What do you want to do\
    Multiplication, Division, Subtraction, Addition, Convert Binary to Base10, Base_8?")
    if Question == "addition" or Question == "Addition":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (addition(var1,var2))
    elif Question == "subtraction" or Question == "Subtraction":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (subtraction(var1,var2))
    elif Question == "Multiplication" or Question == "multiplication":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (multiplication(var1,var2))
    elif Question == "Division" or Question == "division":
        var1 = input("First Number:")
        var2 = input("Second Number:")
        print (division(var1,var2))
    elif Question == "C":
        binary_number = input("Binary Number:")
        print (base2_to_base10(binary_number))
    elif Question == "Base_8":
        binary_number = input("Binary Number:")
        base2_to_base8(binary_number)
    elif Question == "Base_6":
        binary_number = input("Binary Number: ")
        base2_to_base6(binary_number)
Choice()
