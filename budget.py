import datetime
import sys
budgetAccounts = "1. Cash\n 2. Capital One Joint Checking\n 3. Chase Checking\n 4. Ally Savings\n 5. Bank of Hawaii Checking\n 6. Bank of Hawaii Savings\n 7. Venmo (F)\n 8. Venmo (A)\n 9. AMEX Gold\n 10. Hawaiian Airlines Mastercard (F)\n 11. Hawaiian Airlines Mastercard (A)\n 12. Capital One VentureX\n 13. Chase Prime Visa\n 14. Capital One Quicksilver Mastercard\n 15. Chevron (A)\n \n"

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
            #Validating that transaction amount entered by user is a float
            try:
                dollar = float(input("Noooo we spent money. What is the amount? (Don't include the $ sign): "))
            except ValueError:
                print("Invalid dollar amount, please enter again. ")
                continue
            #Asking which budget account the transaction is charging to
            paymentmethod = input("Where are the funds for this transaction coming from?\n " + budgetAccounts)
            memo = input("You can enter a description of the transaction here. ")
            #sys.exit() here to end the script since all the necessary information will have been entered
            sys.exit()
        if cost_or_income == "2":
            dollar = input("Yay we made money. What is the amount? (Don't include the $ sign): ")
            #Asking which budget account the transaction is adding to
            paymentmethod = input("Where is the income going to?\n " + budgetAccounts) 
            memo = input("You can enter a description of the transaction here. ")
        else:
            print("That is not a valid option!")
            continue
        #sys.exit() here to end the script since all the necessary information will have been entered
        sys.exit()
    else:
        #Let user know that date wasn't entered correctly.
        print("Invalid date, please enter again.")