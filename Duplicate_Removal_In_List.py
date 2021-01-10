#This program checks for the duplicate elements in a list and deletes those duplicate elements

sample_list1 = [4,5,2,5.3,4, 2, 3, 5.2, 3.4, 5, 8, 9, 10, 12, 8, 10, 10, 4, 5]
sample_list2 = [4,5,2,5.3,4, 2, 3, 5.2, 3.4, 5, 8, 9, 10, 12, 8, 10, 10, 4, 5]

#Logic_1
def DuplicateRemoval_1(list):
    for i in list:
        if list.count(i) > 1:
            list.remove(i)
    return list


#Logic_2
def DuplicateRemoval_2(list):
    UniqList = []
    for i in list:
        if i not in UniqList:
            UniqList.append(i)
    return UniqList


if __name__ == "__main__":
    print (DuplicateRemoval_1(sample_list1))
    print (DuplicateRemoval_2(sample_list2))

