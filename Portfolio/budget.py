def budget_tracker():
    import math

    budget=float(input("Enter you budget:"))
    expense=float(input("Enter your expenses:"))
    balance=budget-expense
    print(f"You have R{balance} of spending money left for the set duration")

    while balance > 0:
        expense=float(input("Enter your expenses:"))
        balance=balance-expense
        print(f"You have R{balance} of spending money left for the set duration")

        if balance>=(budget/2):
            print("You're in the green zone, keep it ip!")
        elif balance<(budget/2) and balance>0:
            print("You've used up more than half your budget now, be sure to pace yourself.")
        elif balance<=0:
            print("Oops,you've used up your budget for this duration; time to tone it down and plan better.")
        else:print("Error")  