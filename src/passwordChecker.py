## passwordChecker.py
##
## Written by Matthew Egan
## Created: 6th August 2013
## Last Revised: 6th August 2013
##
## For more information: https://github.com/tolo137/PasswordChecker.git

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
    def runLengthTest():
        pass
    def runUppercaseTest():
        pass
    def runLowercaseTest():
        pass
    def runNumberTest():
        pass
    def runSpecialCharTest():
        pass
    def runMiddleCharTest():
        pass
    def runLettersOnlyTest():
        pass
    def runNumbersOnlyTest():
        pass
    def runRepeatingCharTest():
        pass
    def runConsecUpperTest():
        pass
    def runConsecLowerTest():
        pass
    def runConsecNumberTest():
        pass
    def runSequentialLettersTest():
        pass
    def runSequentialNumbersTest():
        pass
    def runDictionaryWordsTest():
        pass

if __name__ == "__main__": passwordChecker()