def calcIntrest(principal, interest_rate, time_period, frequencey):
    amount = principal * (1 + (interest_rate / Compounding_frequencey)) ** (Compounding_frequencey * time_period)
    interestAmt = amount - principal
    return interestAmt
    
    
principal = float(input("Enter principal amount"))
interest_rate = float(input("enter interest rate"))
time_period = float(input("enter time period"))
Compounding_frequencey = float(input("Enter compunding Frequencey"))
amount = principal * (1 + (interest_rate / Compounding_frequencey)) ** (Compounding_frequencey * time_period)


totalInterest = calcIntrest(principal, interest_rate, time_period, Compounding_frequencey)

print("total interest accured: $", round(totalInterest, 2))