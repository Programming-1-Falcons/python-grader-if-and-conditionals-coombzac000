while True:  
    Tot = float(input("How many points can the student get in total (Out of __)?: "))  
    Stu = float(input("How many points did the student get in total? (__/Total): "))  
  
    Percentage = (Stu / Tot) * 100  
    print(f"The student got a percentage of: {Percentage}%")  
  
    if Percentage < 51:  
        print("Grade: F") 
    elif Percentage < 61:
        print("Grade D")
    elif Percentage < 71:
        print("Grade: C")
    elif Percentage < 81:
        print("Grade: B")
    elif Percentage < 100:
        print("Grade A")
    elif Percentage < 90000000000:
        print("Cheater")