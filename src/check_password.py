"""
This script will use passwordChecker module for testing purposes.
"""
import passwordChecker

passwords_to_check = []
passwords_to_check.append("hello")
passwords_to_check.append("heLLo")
passwords_to_check.append("h3LLo")
passwords_to_check.append("H3LL0-tH3R3")

for password in passwords_to_check:
    score = passwordChecker.new_passwordChecker(password).get_score()
    print "The password '%s' got the score %s" % (password, score)
