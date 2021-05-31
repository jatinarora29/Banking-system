import pickle as PK


def saveData(data):
    with open("data.db", "wb") as f:
        PK.dump(data, f)


def loadData():
    with open("data.db", "rb") as f:
        data = PK.load(f)
    return data


def loadLoanData():
    with open("loan.db", "rb") as f:
        loanData = PK.load(f)
    return loanData


def saveLoanData(loanData):
    with open("loan.db", "wb") as f:
        PK.dump(loanData, f)
