import re,random

def strongPasswordDetector():
    password = input()
    upper = re.compile(r'[A-Z]')
    lower = re.compile(r'[a-z]')
    num = re.compile(r'[0-9]')
    specChar = re.compile(r'[!@#$\^&\*\(\):;\'\"<>,\.\?\/|]')

    if re.compile(r'\s').search(password) or len(password) < 8:
        print('Your Password must be atleast 8 characters (without containing spaces) long to be a strong password')
    elif upper.search(password) and lower.search(password) and num.search(password) and specChar.search(password):
        print('This is a strong Password')
    else:
        print('A strong password should contain both UPPERCASE and lowercase letters with atleast one digit and one special character')

strongPasswordDetector()
