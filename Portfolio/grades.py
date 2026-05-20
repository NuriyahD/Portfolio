def grade_calculator():
    grade=int(input("Enter you grade: "))
    num=2
    while True:
        grade2=int(input("Enter your next grade (or enter 111 to exit): "))
        grade=grade+grade2
        avg_grade=round(grade/num,2)
        print(f"Your average is:{avg_grade}")
        num+=1
        if grade2==111:
            break