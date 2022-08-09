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
    if(isValidDate):
        cost_or_income = input("Is this a cost or income? ") 
        dollar = input("What is the amount? ") 
        paymentmethod = input("Where are the funds going to/coming from? ") 
        memo = input("You can enter a description of the transaction here. ")
        #sys.exit() here to end the script since all the necessary information will be gathered
        sys.exit()
    else:
        #Let user know that date wasn't entered correctly.
        print("Invalid date, please enter again.")