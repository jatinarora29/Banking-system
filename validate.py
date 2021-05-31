

def isMobileValid(mobileNo):
    if mobileNo > 999999999 and mobileNo < 10000000000:
        return True
    else:
        return False


def isAadharValid(aadharNo):
    if aadharNo > 99999999999 and aadharNo < 10000000000000:
        return True
    else:
        return False


def isUserValid(accountNo, data, userId, password):
    accountNo = str(accountNo)
    if data[accountNo]['userId'] == userId:
        if data[accountNo]['password'] == password:
            return True
        else:
            return False
    else:
        return False


def isValidPassword(password):
    specialChars = (x for x in "~!@#$%^&*/_-+\\:;?" )
    if len(password) < 8:
        return False
    elif any(x.isdigit() for x in password) and any(x.isupper() for x in password) and any(x in password for x in specialChars):
        # Check for if any of character of the password are digits , uuper case and special character
        return True
    else:
        return False
