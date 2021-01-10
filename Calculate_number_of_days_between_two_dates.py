
# Python program to calculate between two dates

dt1 = 2015, 12, 1
dt2 = 2018, 4, 1


DaysPerMonth = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# function to check leap year
def leapYear(y):
    if y%4 == 0:
        if y%100 == 0:
            if y%400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False


# class to calculate no. of days from 00/00/0000 (dd/mm/yyyy)
class NoOfDays():

    def __init__(self,date):
        self.date = date

    def yearDays(self):
        leapcnt = 0
        for i in range (1, self.date[0]):
            leap = leapYear(i)
            if leap == True:
                leapcnt += 1
        return ((((self.date[0]-1)-leapcnt)*365)+(leapcnt*366))

    def monthDays(self):
        Mdays = 0
        for i in range (1, self.date[1]):
            Mdays += DaysPerMonth[i-1]
        if leapYear(self.date[0]) and self.date[1] > 2:
            Mdays += 1
        return Mdays

    def totalDays(self):
        return (self.yearDays() + self.monthDays() + self.date[2])

difference = NoOfDays(dt1).totalDays() - NoOfDays(dt2).totalDays()
print ("Difference between two dates :",abs(difference),"Days")
