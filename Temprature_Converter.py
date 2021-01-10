# This program can be used to convert temperatures from Celsius to Fahrenheit and vice versa
# Formulae : C = (F - 32) / 1.8
# C = Temperature in Celsius
# F = Temperature in Fahrenheit

def TempConvert():
    print ("\n")
    print ("Temprature Converter Application")
    print ("Designed & Developed by : Vishal Farakate")

    opt = input ("""
    Select your option : 
    1. Celcius to Farenhite
    2. Farenhite to Celcius
    
    """)

    if int(opt) == 1:
        C = input("Enter Temprature in Celcius (degree) : ")
        F = ((int(C))*1.8)+32
        print ("Temprature in Farenhite is",F,"degree")

    elif int(opt) == 2:
        F = input("Enter Temprature in Farenhite (degree) : ")
        C = ((int(F))-32)/1.8
        print ("Temprature in Celcius is",C,"degree")

    else:
        print ("Invalid Input")

TempConvert()






