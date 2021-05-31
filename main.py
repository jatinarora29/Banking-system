from intro import menu, bankingMenu, intro
import SaveData as SD
from loan import loan
from account import *

data = SD.loadData()


keyList = list(data.keys())
adminUserId = data[keyList[0]]['userId']
adminPassword = data[keyList[0]]['password']
accountNo = int(keyList[-1]) + 1


intro()


while True:
    try:
        menu()
        ch = int(input("\n\t\t Enter your choice : "))
        if ch == 1:
            while True:
                try:
                    bankingMenu()
                    ch = int(input('\n\t\t Enter your choice : '))

                    if ch == 1:
                        accountNo, data = createAccount(accountNo, data)
                        accountFunctionality(accountNo, data)
                    elif ch == 2:
                        while True:
                            try:
                                userAccountNo = int(
                                    input('\t\t Enter your account number : '))
                                userId = input('\t\t Enter your user ID : ')
                                password = gtps.getpass(
                                    prompt='\t\t Enter your password : ')
                            except Exception as e:
                                print('\t\t Please enter s valid credentials ')
                            else:
                                break
                        if str(userAccountNo) in data.keys():

                            if data[str(userAccountNo)]['userId'] == userId:
                                if data[str(userAccountNo)]['password'] == password:
                                    accountFunctionality(userAccountNo, data)
                                else:
                                    print('\t\t Enter a valid password ')
                            else:
                                print('\t\t User Id does not match ')
                        else:
                            print('\t\t Enter a valid account number ')
                    elif ch == 3:
                        try:
                            userAccountNo = int(
                                input('\t\t Enter your account number : ')
                            )
                            if str(userAccountNo) in data.keys():
                                data = internetBanking(userAccountNo, data)
                        except:
                            print('\n\t\t Please enter a valid account number')

                    elif ch == 4:
                        break
                    else:
                        print('\t\t Please enter a valid choice ')
                except ValueError:
                    print('\t\t Enter a valid choice ')
        elif ch == 2:
            loan(data)
        elif ch == 3:
            managerUserId = input('\t\t Enter user ID : ')
            managerPassword = gtps.getpass(
                prompt='\t\t Enter your password : ')
            if managerUserId == adminUserId and managerPassword == adminPassword:
                i = 1
                for keys in data.keys():
                    if i == 1:
                        i += 1
                        continue

                    print(f"\n\t\t Name : {data[keys]['name']}")
                    print(f"\t\t Address : {data[keys]['address']}")
                    print(f"\t\t Mobile number : {data[keys]['mobileNo']}")
                    print(f"\t\t Date of Birth : {data[keys]['dateOfBirth']}")
                    print(
                        f"\t\t Account Balance : {data[keys]['accountBalance']}\n")
            else:
                print('\n\t\t Your userId or password is invalid\n')

        elif ch == 4:
            break
        else:
            print('\n\t\t Enter a valid choice\n')
    except ValueError:
        print('\n\t\t Enter a valid choice\n')
