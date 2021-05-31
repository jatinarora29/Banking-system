from datetime import date as DT, timedelta as TMDL
from intro import emiMenu
from SaveData import saveLoanData as SLD, loadLoanData as LLD, saveData
import getpass as gtps


def laonIssue(accountNo, loanAmount, emiTime, installmentDate, installmentAmount):
    """ Takes accountNo , loanAmount , emiTime , and installmentDate as input parameters and Creates a 
    dictionary of information related to loan and Open loan.db file and store the information in it 
    """
    try:
        loanInfo = {
            "loanAmount": loanAmount,
            "installmentDate": installmentDate,
            "installmentAmount": installmentAmount,
            "loanIssueDate": str(DT.today()),
            "emiTime": emiTime,
            "interst": 7,
            "loanPeriod": str(DT.today() + TMDL(days=1095))
        }
        loanData = LLD()
        loanData[accountNo] = loanInfo
        SLD(loanData)
        print(
            f"\n\t\t loan issued of amount {loanAmount} with interst of 7 % for a total period of 3 years \n"
        )
    except Exception as e:
        print(e)


def firstInstallmentCalculator(emiTime):
    """ Takes emiTime as input and calculates the last date of returning the loan's first installment
    and returns the date as installmentDate
    """
    if emiTime == 3:
        installmentDate = str(DT.today() + TMDL(days=90))
    elif emiTime == 6:
        installmentDate = str(DT.today() + TMDL(days=180))
    elif emiTime == 9:
        installmentDate = str(DT.today() + TMDL(days=270))
    else:
        installmentDate = str(DT.today() + TMDL(days=365))

    return installmentDate


def loanEMI(loanAmount):
    while True:
        try:
            emiMenu()
            ch = int(input('\t\t Enter your choice : '))
            if ch == 1:
                emiTime = 3
                installmentDate = firstInstallmentCalculator(emiTime)
                installmentAmount = loanAmount // 12
            elif ch == 2:
                emiTime = 6
                installmentDate = firstInstallmentCalculator(emiTime)
                installmentAmount = loanAmount // 6
            elif ch == 3:
                emiTime = 9
                installmentDate = firstInstallmentCalculator(emiTime)
                installmentAmount = loanAmount // 4
            elif ch == 4:
                emiTime = 12
                installmentDate = firstInstallmentCalculator(emiTime)
                installmentAmount = loanAmount // 3
            else:
                print("\t\t Enter a valid choice ")
                continue
            return installmentDate, installmentAmount, emiTime

        except:
            print("\t\t Enter a valid choice ")


def salary(accountNo):
    """ Takes accountNo as input and ask user to provide salary and check the eligible loan amount and 
    then calculates the installmentDate, emiTime, LoanAmount with the help of LoanEMI, 
    function and calls loanIssue function to issue loan
    """
    while True:
        try:
            salary = int(input('\t\t Enter your salary : '))
            if salary >= 3*(10**5):
                print("\n\t\t You are eligible for loan upto 5 lakhs on interst of 7%")
                ch = input('\t\t Do you have salary slip Y/N : ')
                if ch.strip().lower() == 'y':
                    loanAmount = 5*(10**5)
                else:
                    print("\n\t\t Sorry, But you are not eligible for loan \n")

            elif salary >= 10**5:
                print("\n\t\t You are eligible for loan upto 3 lakhs on interst of 7%")
                ch = input('\t\t Do you have salary slip Y/N : ')
                if ch.strip().lower() == 'y':
                    loanAmount = 3*(10**5)
                else:
                    print("\n\t\t Sorry, But you are not eligible for loan \n")

            elif salary >= 5*(10**4):
                print("\n\t\t You are eligible for loan upto 2 lakhs on interst of 7%")
                ch = input('\t\t Do you have salary slip Y/N : ')
                if ch.strip().lower() == 'y':
                    loanAmount = 2*(10**5)
                else:
                    print("\n\t\t Sorry, But you are not eligible for loan \n")

            else:
                print("\t\t You are not eligible for loan !")
                break
            installmentDate, installmentAmount, emiTime = loanEMI(loanAmount)
            laonIssue(accountNo, loanAmount, emiTime,
                      installmentDate, installmentAmount)
            break
        except:
            print("\t\t Please enter a valid amount")


def loan(data):
    loanData = LLD()
    while True:
        try:
            accountNo = input('\t\t Enter your account number : ')
            if accountNo in data.keys():
                break
            print("\n\t\t This account is not part of our bank")
        except:
            print("\n\t\t Enter a valid account number")

    while True:
        print("\n\t\t 1. Get loan ")
        print("\t\t 2. View loan ")
        print("\t\t 3. Pay installment ")
        ch = int(input("\t\t Enter your choice : "))
        if ch == 1:
            if not loanData.get(accountNo):
                while True:
                    try:
                        print("\t\t What is your working status ")
                        print("\t\t 1. Student ")
                        print("\t\t 2. Government Empoyee ")
                        print("\t\t 3. Private Empoyee ")
                        print("\t\t 4. Business ")
                        print("\t\t 5. Exit ")
                        ch = int(input('\t\t Enter your choice : '))
                        if ch == 1:
                            print(
                                "\n\t\t Sorry, But you are not eligible for loan \n")

                        elif ch == 2 or ch == 3 or ch == 4:
                            salary(accountNo)

                        elif ch == 5:
                            break
                        else:
                            print("\t\t Enter a valid choice")
                            continue
                        break

                    except:
                        print("\n\t\t Enter a valid choice")

                break
            else:
                print("\n\t\t You already have a loan issued")
                print("\t\t Please pay that first")

        elif ch == 2:
            if loanData.get(accountNo):
                print(
                    f"\n\t\t You have a panding loan of amount : {loanData[accountNo]['loanAmount']}")
                if str(DT.today()) == loanData[accountNo]['installmentDate']:
                    emiTime = loanData[accountNo]['emiTime']
                    loanData[accountNo]['installmentDate'] = str(
                        DT.today() + TMDL(days=(emiTime*30))
                    )
                    SLD(loanData)
                installmentDate = loanData[accountNo]['installmentDate']
                print(
                    f"\n\t\t Your date of next installment is : {installmentDate}")
            else:
                print("\n\t\t You haven't taken any loan ")

        elif ch == 3:
            password = gtps.getpass(prompt="\t\t Enter your password : ")
            if password == data[accountNo]['password']:
                installmentAmount = loanData[accountNo]['installmentAmount']
                if loanData[accountNo]['loanAmount'] > 10:
                    loanData[accountNo]['loanAmount'] = loanData[accountNo]['loanAmount'] - \
                        installmentAmount
                SLD(loanData)
                print("\n\t\t You have paid your installment ")
            else:
                print("\n\t\t You have entered wrong password")
        else:
            print("\n\t\t Please enter a valid choice")
            continue
        break
