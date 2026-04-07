#Display simple intrest and compound intrest.
P = int(input("Enter the principal: "))
T = int(input("Enter the time: "))
R = int(input("Enter the rate of interest: "))

simple_interest = (P * R * T) / 100

compound_amount = P * (1 + R/100)**T
compound_interest = compound_amount - P 

print("Simple Interest:", simple_interest)
print("Compound Interest:", compound_interest)
