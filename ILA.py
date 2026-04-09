name = input("Enter student's name: ")
grade = int(input("Enter student's grade: "))

if grade >= 90:
    classification = "Satisfactory"
    pf = "passed"
    
elif grade >= 80:
    classification = "Great"
    pf = "passed"
    
elif grade >= 70:
    classification = "Fair"
    pf = "passed"
    
elif grade >= 65:
    classifcation = "Unsatisfactory"
    pf = "passed"
    
else:
    classification = "Bad"
    pf = "failed"


print("")
print(f"Student's Name: {name}")
print(f"Student's Grade {grade}")

if grade >=65:
    print(f"Congratulations {name}! You {pf} with a {classification} grade!")
    
else:
    print(f"{name}, you have {pf} with a {classification} grade.")
