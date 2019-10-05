'''
Created on 11/28/18
@author:   Luke McEvoy
Pledge:    I pledge my honor I have abided by the Stevens Honor Systemw

CS115 - Hw 11/12 - Date class
'''
DAYS_IN_MONTH = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

class Date(object):
    '''A user-defined data structure that stores and manipulates dates.'''

    # The constructor is always named __init__.
    def __init__(self, month, day, year):
        '''The constructor for objects of type Date.'''
        self.month = month
        self.day = day
        self.year = year

    # The 'printing' function is always named __str__.
    def __str__(self):
        '''This method returns a string representation for the
           object of type Date that calls it (named self).

             ** Note that this _can_ be called explicitly, but
                it more often is used implicitly via the print
                statement or simply by expressing self's value.'''
        return '%02d/%02d/%04d' % (self.month, self.day, self.year)

    # Here is an example of a 'method' of the Date class.
    def isLeapYear(self):
        '''Returns True if the calling object is in a leap year; False
        otherwise.'''
        if self.year % 400 == 0:
            return True
        if self.year % 100 == 0:
            return False
        if self.year % 4 == 0:
            return True
        return False

    def copy(self):
    #Returns a new object of same content as shown object
        #Tests memory addresses
        dnew = Date(self.month, self.day, self.year)
        return dnew

    def equals(self, d2):
    #returns if the dates are the same, individually breaks down elements
        #Doesn't test memory addresses
        return self.year == d2.year and self.month == d2.month and \
               self.day == d2.day

    def tomorrow(self):
    #updates self to the date it would be tomorrow
        if self.isLeapYear() and self.month == 2 and self.day == 28:
            self.day = 29
        else:
            if self.day >= DAYS_IN_MONTH[self.month]:
                self.day = 1
                if self.month == 12:
                    self.month = 1
                    self.year = self.year + 1
                else:
                    self.month = self.month + 1
            else:
                self.day = self.day + 1

    def yesterday(self):
    #updates self to the date it was yesterday
        if self.isLeapYear() and self.month == 3 and self.day == 1:
            self.month = 2
            self.day = 29
        else:
            if self.day == 1 and self.month == 1:
                self.month = 12
                self.day = 31
                self.year = self.year - 1
            else:
                if self.day > 1:
                    self.day = self.day - 1
                else:
                    if self.month > 1:
                        self.day = DAYS_IN_MONTH[self.month - 1]
                        self.month = self.month - 1
                    else:
                        self.day = 1

    def addNDays(self, num):
    #add num days to self
        print(str(self))
        for i in range(num):
            self.tomorrow()
            print(str(self))

    def subNDays(self, num):
    #subtracts num days to self
        print(str(self))
        for i in range(num):
            self.yesterday()
            print(str(self))

    def isBefore(self, d2):
    #boolean to check if self is before date2
        if self.year < d2.year:
            return True
        elif self.month < d2.month and self.year == d2.year:
            return True
        elif self.day < d2.day and self.month == d2.month and self.year \
             == d2.year:
            return True
        else:
            return False

    def isAfter(self, d2):
    #boolean to check if self is after date 2
        if self.year > d2.year:
            return True
        elif self.month > d2.month and self.year == d2.year:
            return True
        elif self.day > d2.day and self.month == d2.month and \
             self.year == d2.year:
            return True
        else:
            return False

    def diff(self, d2):
        first = self.copy()
        second = d2.copy()
        result = 0
        if first.isBefore(second):
            while first.isBefore(second):
                first.tomorrow()
                result = result + 1
            result = result * -1
            return result
        else:
            while second.isBefore(first):
                second.tomorrow()
                result = result + 1
            return result

    def dow(self):
        #Return a string that indicates the day of the week (dow) of the object
        key = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        knownW = Date(11,7,2011)
        difference = self.diff(knownW)
        var = difference % 7
        return key[var]
        
                
        
     
