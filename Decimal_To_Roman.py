
# Converting Decimal Number lying between 1 to 3999 to Roman Numerals

number = 381

# Logic - 1
def decimalToRoman_1(number):
    print ()
    print ("Python programme to Convert Decimal Number (lying between 1 to 3999) to Roman Numerals - Logic 1")
    print ()

    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

    for i in range(13):
        div = number // num[12-i]
        if div:
            print ((sym[12-i])*div, end="")
            number = number % num[12-i]
            if number == 0:
                break

decimalToRoman_1 (number)
print ()


# Logic - 2
def decimalToRoman_2(number):
    print ()
    print ("Python programme to Convert Decimal Number (lying between 1 to 3999) to Roman Numerals - Logic 2")
    print ()

    num = [1,4,5,9,10,40,50,90,100,400,500,900,1000]
    sym = ['I','IV','V','IX','X','XL','L','XC','C','CD','D','CM','M']

    i = 12
    while number:
        div = number // num[i]
        number %= num[i]

        while div:
            print (sym[i], end="")
            div -= 1
        i -= 1

decimalToRoman_2(number)
print ()



# Logic - 3
def decimalToRoman_3(number):
    print ()
    print ("Python programme to Convert Decimal Number (lying between 1 to 3999) to Roman Numerals - Logic 3")
    print ()

    sym_fourth = ['','M','MM','MMM']
    sym_third = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    sym_second = ['','X','XX','XXX', 'XL','L','LX','LXX','LXXX','XC']
    sym_first = ['','I','II','III','IV','V','VI','VII','VIII','IX']

    print (sym_fourth[number//1000],end="")
    print (sym_third[(number%1000)//100],end="")
    print (sym_second[(number%100)//10],end="")
    print (sym_first[number%10],end="")

decimalToRoman_3(number)
print()


