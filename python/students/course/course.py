def course():
    print("available courses:")
    course = ["python","java","c programing ","web dovelopment"]
    print(course)
    
    choice=input("please enter the choice:")
    if choice in course:
        print("available course",choice)
    else:
        print("course is found ")
        
        