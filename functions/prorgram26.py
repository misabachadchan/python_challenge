def compound_interest(P, R, T):
    return P * (1 + R/100) ** T

P = float(input("Enter principal: "))
R = float(input("Enter rate (%): "))
T = float(input("Enter time in years: "))
print("Compound Interest:", compound_interest(P, R, T))
