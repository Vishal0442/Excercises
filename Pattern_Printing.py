#This program is for printing different patterns using loops


# Simple Pyramid Pattern - Logic 1
def SimplePyramid_1(n):
    print ("\n")
    print ("Simple Pyramid Pattern - Logic 1")
    print ("\n")

    for i in range (n):
        for j in range (i+1):
            print ("*", end=" ")
        print ("")

SimplePyramid_1(5)


# Simple Pyramid Pattern - Logic 2
def SimplePyramid_2(n):
    print ("\n")
    print ("Simple Pyramid Pattern - Logic 2")
    print ("\n")

    starlist = []
    for i in range (1,n+1):
        starlist.append("* "*i)
    print ("\n".join(starlist))

SimplePyramid_2(7)


# Simple Pyramid Pattern After 180 degree Rotation - Logic 1
def SimplePyramid180_1(n):
    print ("\n")
    print ("Simple Pyramid Pattern After 180 degree Rotation - Logic 1")
    print ("\n")

    k = (n*2)-2
    for i in range(1,n+1):
        space = (" " * k)
        star = ("* " * i)
        print (space,star)
        k -= 2

SimplePyramid180_1(5)


# Simple Pyramid Pattern After 180 degree Rotation - Logic 2
def SimplePyramid180_2(n):
    print ("\n")
    print ("Simple Pyramid Pattern After 180 degree Rotation - Logic 2")
    print ("\n")

    k = (n*2)-2
    for i in range(1,n+1):
        for j in range (k):
            print (end=" ")

        k -= 2

        for j in range(i):
            print ("*", end=" ")
        print ()

SimplePyramid180_2(7)


# Triangle Pattern - Logic 1
def Triangle_1(n):
    print ("\n")
    print ("Triangle Pattern - Logic 1")
    print ("\n")

    k = n-1
    for i in range(1,n+1):
        space = (" " * k)
        star = ("* " * i)
        print (space,star)
        k -= 1

Triangle_1(5)


# Triangle Pattern - Logic 2
def Triangle_2(n):
    print ("\n")
    print ("Triangle Pattern - Logic 2")
    print ("\n")

    k = n-1
    for i in range(1,n+1):

        for j in range(k):
            print (end=" ")
        k -= 1

        for j in range (i):
            print ("*", end=" ")
        print ()

Triangle_2(8)


# Triangle Pattern after 90 degree rotation - Logic 1

def Triangele_90degree_1(n):
    print ("\n")
    print ("Triangle Pattern after 90 degree rotation - Logic 1")
    print ("\n")

    for i in range(1,n+1):
        print ("* "*i)
    for i in range(1,n+1):
        print ("* "*(n-i))

Triangele_90degree_1(4)


# Triangle Pattern after 90 degree rotation - Logic 2

def Triangele_90degree_2(n):
    print ("\n")
    print ("Triangle Pattern after 90 degree rotation - Logic 2")
    print ("\n")

    for i in range(n):
        for j in range(i):
            print ("*", end=" ")
        print()
    for i in range(n,0,-1):
        for j in range(i):
            print ("*", end=" ")
        print()

Triangele_90degree_2(4)


# Number Pattern - Logic 1
def Number_1(n):
    print ("\n")
    print ("Number Pattern - Logic 1")
    print ("\n")

    for i in range(1,n+1):
        for j in range(1,i+1):
            print (j, end=" ")
        print ()

Number_1(8)


# Character Pattern
def Character(n):
    print ("\n")
    print ("Character Pattern")
    print ("\n")

    #ASCII value
    base_chr = 65

    for i in range(1,n+1):
        for j in range(i):
            print (chr(base_chr+j), end=" ")
        print ()

Character(10)


# Continuous Character Pattern
def ContinuousCharacter(n):
    print ("\n")
    print ("Continuous Character Pattern")
    print ("\n")

    #ASCII value
    base_chr = 65

    num = 0
    for i in range(1,n+1):
        for j in range(i):
            print (chr(base_chr+num), end=" ")
            num += 1
        print ()

ContinuousCharacter(6)
