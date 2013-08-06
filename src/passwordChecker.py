## passwordChecker.py
##
## Written by Matthew Egan
## Created: 6th August 2013
## Last Revised: 6th August 2013
##
## For more information: https://github.com/tolo137/PasswordChecker.git

import string

class passwordChecker:
    def __init__(self):
        self.getPassword()
        self.score = 0
        self.runPasswordTests()
    def getPassword(self):
        self.password = raw_input("Enter the password you want to check: ")
    def displayPassword(self):
        print self.password
    def changeScore(self, val):
        self.score = self.score + val
    def runPasswordTests(self):
        self.runLengthTest()
        self.runUppercaseTest()
        self.runLowercaseTest()
        self.runNumberTest()
        self.runSpecialCharTest()
        self.runMiddleCharTest()
        self.runLettersOnlyTest()
        self.runNumbersOnlyTest()
        self.runRepeatingCharTest()
        self.runConsecUpperTest()
        self.runConsecLowerTest()
        self.runConsecNumberTest()
        self.runSequentialLettersTest()
        self.runSequentialNumbersTest()
        self.runDictionaryWordsTest()
        print "\nThe password score was:", self.score
        if self.score < 0:
            print "Very bad password"
        elif self.score >= 0:
            print "Bad password"
        elif self.score >= 30:
            print "Ok password"
        elif self.score >= 60:
            print "Better password"
        elif self.score >= 80:
            print "Awesome password"
    def runLengthTest(self):
        """ Assesses the length of a password and 
            increments the score by the length """
        length = len(self.password)
        self.changeScore(length)
    def runUppercaseTest(self):
        """ Assesses how many uppercase letters
            are in a password and increments the
            score by that amount """
        upperCaseCount = 0
        for index in self.password:
            if index in string.uppercase:
                upperCaseCount += 1
        self.changeScore(upperCaseCount)
    def runLowercaseTest(self):
        """ Assesses how many lowercase letters
            are in a password and increments the 
            score by that amount """
        lowerCaseCount = 0
        for index in self.password:
            if index in string.lowercase:
                lowerCaseCount += 1
        self.changeScore(lowerCaseCount)
    def runNumberTest(self):
        """ Assesses how many numeric characters
            are in a password and increments the
            score by that amount """
        numberCount = 0
        for index in self.password:
            if index in string.digits:
                numberCount += 1
        self.changeScore(numberCount)
    def runSpecialCharTest(self):
        """ Assesses how many special characters
            are in a password and increments the
            score by that amount """
        specialCount = 0
        for index in self.password:
            if index in string.punctuation:
                specialCount += 1
        self.changeScore(specialCount)
    def runMiddleCharTest(self):
        pass
    def runLettersOnlyTest(self):
        pass
    def runNumbersOnlyTest(self):
        pass
    def runRepeatingCharTest(self):
        pass
    def runConsecUpperTest(self):
        pass
    def runConsecLowerTest(self):
        pass
    def runConsecNumberTest(self):
        pass
    def runSequentialLettersTest(self):
        pass
    def runSequentialNumbersTest(self):
        pass
    def runDictionaryWordsTest(self):
        pass

class new_passwordChecker:
    def __init__(self, password):
        self.password = password
        #Calculating the score
        self.score = 0
        self.score += self.__lenght_score()
        self.score += self.__uppercase_score()
        self.score += self.__lowercase_score()
        self.score += self.__digits_score()
        self.score += self.__special_score()
    
    def __lenght_score(self):
        return len(self.password)
    
    def __uppercase_score(self):
        score = 0
        for char in self.password:
            if char in string.uppercase:
                score += 1
        return score
    
    def __lowercase_score(self):
        score = 0
        for char in self.password:
            if char in string.lowercase:
                score += 1
        return score
    
    def __digits_score(self):
        score = 0
        for char in self.password:
            if char in string.digits:
                score += 1
        return score
    
    def __special_score(self):
        score = 0
        for char in self.password:
            if char in string.punctuation:
                score += 1
        return score
    
    def get_score(self):
        return self.score
    
    def get_readable_score(self):
        if self.score < 0:
            return "Very weak"
        elif self.score >= 0:
            return "Weak"
        elif self.score >= 30:
            return "OK"
        elif self.score >= 60:
            return "Strong"
        elif self.score >= 80:
            return "Very strong"
