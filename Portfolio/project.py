while True:
    print("1. Budget reporter")
    print("2. Even/Odd Checker")
    print("3. Grade Calculator")
    print("4. Exit")

    choice=input("Choose an option:")

    if choice=="1":
        import budget
        budget.budget_tracker()
    elif choice=="2":
        import eoc
        eoc.even_or_odd_checker()
    elif choice=="3":
        import grades
        grades.grade_calculator()
    elif choice=="4":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")