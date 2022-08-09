import datetime
import sys

# While True entered here so that it loops back to asking for date input if invalid date is entered
while True:
    inputDate = input("Enter the date of the transaction in mm/dd/yyyy format: ")
    month,day,year = inputDate.split('/')

    isValidDate = True
    try:
        #Order of datetime.datetime needs to be largest to smallest (year, month, day, etc.)
        datetime.datetime(int(year),int(month),int(day))
    except ValueError:
        isValidDate = False
    #If isValidDate is TRUE, then it will run the "if" portion
    while(isValidDate):
        cost_or_income = input("Is this a cost or income? Type '1' for cost and '2' for income: ")
        while cost_or_income == "1":
            try:
                dollar = float(input("Noooo we spent money. What is the amount? (Don't include the $ sign): "))
            except ValueError:
                print("Invalid dollar amount, please enter again. ")
                continue
            paymentmethod = input("Where are the funds for this transaction coming from? ")
            memo = input("You can enter a description of the transaction here. ")
            sys.exit()
        if cost_or_income == "2":
            dollar = input("Yay we made money. What is the amount? (Don't include the $ sign): ")
            paymentmethod = input("Where is the income going to? ") 
            memo = input("You can enter a description of the transaction here. ")
        else:
            print("That is not a valid option!")
            continue
        #sys.exit() here to end the script since all the necessary information will be gathered
        sys.exit()
    else:
        #Let user know that date wasn't entered correctly.
        print("Invalid date, please enter again.")