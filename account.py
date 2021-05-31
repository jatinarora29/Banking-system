from datetime import date as DT
import validate as VD
import getpass as gtps
import SaveData as SD
from intro import accountMenu, updateAccountMenu


def createAccount(accountNo, data):
    """  CreateAccount  takes accountno and data(old information releated to account) as input to function
    and create new account by taking name ,address,dateofbirth , mobileno , aadharNo ,userid and password
    and save it to data.db file   
    """
    while True:
        specialChars = (x for x in '~!@#$%^&*_-+=:;/?\\')
        name = input('\t\t Enter your full name : ')
        if not any(x.isdigit()
                   for x in name) and not any(x in name for x in specialChars):
            break
        print('\t\t Enter a valid name ')
    address = input('\t\t Enter your address : ')
    while True:  # loop run till a valid date of birth is entered
        try:
            print('\t\t Enter your date of birth : ')
            day = int(input('\t\t Enter your date : '))
            month = int(input('\t\t Enter your month : '))
            year = int(input('\t\t Enter your year : '))
            if day > 0 and day < 32 and month > 0 and month < 13 and year > 1990 and year < DT.today().year:
                # * Checking if day , month and year is valid
                break
            print("\t\t Please Enter a valid date of birth")
        except Exception as e:
            print("\t\t Please Enter a valid date of birth")
    dateOfBirth = DT(year, month, day)
    while True:
        try:
            mobileNo = int(input('\t\t Enter your 10 digits Mobile no. : '))
            if VD.isMobileValid(mobileNo):  # Checking if Mobile no is valid
                break
            print("\t\t Please enter a valid mobile number ")
        except Exception as e:
            print("\t\t Please enter a valid mobile number ")
    while True:
        try:
            aadharNo = int(input('\t\t Enter your Aadhar number : '))
            if VD.isAadharValid(aadharNo):  # Checking if aadhar is valid
                break
            print("\t\t Please enter a valid Aadhar number ")
        except Exception as e:
            print("\t\t Please enter a valid Aadhar number ")
    while True:
        try:
            balance = int(input('\t\t Enter your starting balance : '))
            if balance > 1000:  # assuring 1000 as minimum balance
                break
            print("\t\t Please enter a amount greater than 1000 ")
        except ValueError:
            print("\t\t Please enter a valid amount ")
    if input('\t\t Press Y of internet banking : ').strip().lower() == 'y':
        while True:
            userId = input('\t\t Enter your user ID : ')
            if userId != name:
                break
            print("\t\t Please enter a different user ID ")
        while True:
            password = gtps.getpass(prompt='\t\t Enter your password : ')
            if VD.isValidPassword(password):
                cPassword = gtps.getpass(
                    prompt='\t\t Confirm your password : ')
                if password == cPassword:
                    break
                else:
                    print('\t\t Confirm password not match ')
            print(
                "\n\t\t Please enter a valid password with at least 1 uppercase , 1 number and 1 special character\n"
            )
    else:
        userId = None
        password = None

    accountDetails = {
        'name': name,
        'address': address,
        'dateOfBirth': str(dateOfBirth),
        'mobileNo': mobileNo,
        'aadharNo': aadharNo,
        'accountBalance': balance,
        'userId': userId,
        'password': password
    }

    data[str(accountNo)] = accountDetails
    print('\n\t\t Account has been created ')
    print(f'\t\t Your account number is : {accountNo}\n')
    SD.saveData(data)
    return accountNo, data


def internetBanking(accountNo, data):

    while True:
        userId = input('\t\t Enter user ID : ')
        if userId != data[str(accountNo)]['name']:
            break
        print('\t\t Please enter a new user ID ')
    while True:
        password = gtps.getpass(prompt='\t\t Enter your password : ')
        if VD.isValidPassword(password):
            i = 1
            while i <= 3:
                cPassword = gtps.getpass(
                    prompt='\t\t Confirm your password : ')
                if password == cPassword:
                    break
                else:
                    print('\t\t Confirm password not match ')
                i += 1
            break
        print(
            "\n\t\t Please enter a valid password with at least 1 uppercase , 1 number and 1 special character\n"
        )

    if i == 4:
        print('\n\t\t You have exceeded the maximum limit of attempts \n\t\t Try again later\n')
    else:
        data[str(accountNo)]['userId'] = userId
        data[str(accountNo)]['password'] = password
        SD.saveData(data)
        print("\n\t\t Your internet banking has been successfully updated ")
        print(f"\t\t Your internet banking userId is : {userId}\n")

    return data


def changeMobile(accountNo, data):
    while True:
        try:
            mobileNo = int(input('\t\t Enter your mobile number : '))
            if VD.isMobileValid(mobileNo):
                data[str(accountNo)]['mobileNo'] = mobileNo
                SD.saveData(data)
                print('\n\t\t Your mobile number successfully updated \n')
                break
            print('\t\t Enter a valid mobile number ')
        except ValueError:
            print('\t\t Enter a valid mobile number ')
    return data


def changeAadhar(accountNo, data):
    while True:
        try:
            aadharNo = int(input('\t\t Enter your aadhar number : '))
            if VD.isAadharValid(aadharNo):
                data[str(accountNo)]['aadharNo'] = aadharNo
                SD.saveData(data)
                print('\n\t\t Your aadhar number successfully updated \n')
                break
            print('\t\t Enter a valid aadhar number ')
        except ValueError:
            print('\t\t Enter a valid aadhar number ')
    return data


def changeAddress(accountNo, data):
    address = input('\t\t Enter your address : ')
    data[str(accountNo)]['address'] = address
    SD.saveData(data)
    print('\n\t\t Your address has been successfully updated\n ')
    return data


def accountFunctionality(accountNo, data):
    while True:
        try:
            accountMenu()
            ch = int(input("\t\t Enter your choice : "))
            if ch == 1:
                print(
                    f"\n\t\t Your Account balance is : {data[str(accountNo)]['accountBalance']}\n "
                )
            elif ch == 2:
                try:
                    amount = int(
                        input("\t\t Enter the amount to deposit : ")
                    )
                    if amount > 0:
                        data[str(accountNo)]['accountBalance'] = data[str(
                            accountNo)]['accountBalance'] + amount
                        print(
                            f"\n\t\t Your Account balance is : {data[str(accountNo)]['accountBalance']} \n"
                        )
                        SD.saveData(data)
                    else:
                        print("\n\t\t Please enter amount greater than 0")
                except:
                    print("\n\t\t Enter a valid amount")
            elif ch == 3:
                try:
                    amount = int(
                        input("\t\t Enter the amount to withdraw : ")
                    )
                    if amount >= 1000 and amount < data[str(accountNo)]['accountBalance'] - 1000:
                        data[str(accountNo)]['accountBalance'] = data[str(
                            accountNo)]['accountBalance'] - amount
                        print(
                            f"\n\t\t Your Account balance is : {data[str(accountNo)]['accountBalance']} \n"
                        )
                        SD.saveData(data)
                    else:
                        print('\t\t Enter amount greater then or equal to 1000')
                except:
                    print('\n\t\t Please enter a valid amount')

            elif ch == 4:
                data = internetBanking(accountNo, data)
            elif ch == 5:
                while True:
                    try:
                        updateAccountMenu()
                        ch = int(input('\t\t Enter your choice : '))
                        if ch == 1:
                            data = changeMobile(accountNo, data)
                        elif ch == 2:
                            data = changeAadhar(accountNo, data)
                        elif ch == 3:
                            data = changeAddress(accountNo, data)
                        elif ch == 4:
                            break
                        else:
                            print("\t\t Enter a valid choice ")
                            continue
                        break
                    except :
                        print("\n\t\t Enter a valid choice")
            elif ch == 6:
                break
            else:
                print("\t\t Enter a valid choice ")
        except Exception as e:
            print("\n\t\t Enter a valid choice ")
