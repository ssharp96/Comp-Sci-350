# Average Test Grades
# author: SSharp

def grade (totalPoints,numTests):
    return totalPoints/numTests

numTests = int(input("How many tests have you taken? (Between 0 and 6) "))

if numTests == 1:
    a = int(input("What was your grade on test 1? "))
    totalPoints = a
elif numTests == 2:
    a = int(input("What was your grade on test 1? "))
    b = int(input("What was your grade on test 2? "))
    totalPoints = a+b
elif numTests == 3:
    a = int(input("What was your grade on test 1? "))
    b = int(input("What was your grade on test 2? "))
    c = int(input("What was your grade on test 3? "))
    totalPoints = a+b+c
elif numTests == 4:
    a = int(input("What was your grade on test 1? "))
    b = int(input("What was your grade on test 2? "))
    c = int(input("What was your grade on test 3? "))
    d = int(input("What was your grade on test 4? "))
    totalPoints = a+b+c+d
elif numTests == 5:
    a = int(input("What was your grade on test 1? "))
    b = int(input("What was your grade on test 2? "))
    c = int(input("What was your grade on test 3? "))
    d = int(input("What was your grade on test 4? "))
    e = int(input("What was your grade on test 5? "))
    totalPoints = a+b+c+d+e
elif numTests == 6:
    a = int(input("What was your grade on test 1? "))
    b = int(input("What was your grade on test 2? "))
    c = int(input("What was your grade on test 3? "))
    d = int(input("What was your grade on test 4? "))
    e = int(input("What was your grade on test 5? "))
    f = int(input("What was your grade on test 6? "))
    totalPoints = a+b+c+d+e+f

avg = grade(totalPoints,numTests)

print("Your overall test average in the class is",avg)

if avg >= 85:
    print("Nice job!")
elif 70 <= avg < 85:
    print("Pretty good.")
else:
    print("Get your life together.")
    
    
