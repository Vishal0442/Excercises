#this program checks whether 2 lists have any one common element
#if common element found, it return True, else False

numlist1 = ["a", 2, 4, 5, 2.3, 4, 8, 2, 3, 4.6, 8, 10, 4]
numlist2 = [2, 4, 8, 6, 19, 17, 4.5]
numlist3 = [1, 7, 11, 13, 21, "A"]


#Logic_1
def Chklist_1(list1, list2):
    flag = False
    for i in list1:
        if i in list2:
            flag = True
            break
    return flag


#Logic_2
# return method breaks all loops and goes to function caller, hence we can skip use of flag and break function
def Chklist_2(list1, list2):
    for i in list1:
        if i in list2:
            return True


if __name__ == "__main__":
    print (Chklist_1(numlist1, numlist2))
    print (Chklist_1(numlist1, numlist3))

    print (Chklist_2(numlist1, numlist2))
    print (Chklist_2(numlist1, numlist3))


