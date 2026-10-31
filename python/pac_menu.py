import indixpert_Tasks.python.package as package 

def menu():
    dic={}
    while True:
        print("1.signup")
        print("2.login")
        print("3.profile")
        print("4.course")
        print("5.search")
        print("6.exit")
        choice = int(input("please enter the choice:"))
        
        if choice ==1:
            package.signup.signup(dic)
        elif choice ==2:
            package.login.login(dic)
        elif choice ==3: 
            package.profile.profile(dic)
        elif choice ==4: 
            package.course.course(dic)
        elif choice ==5:    
            package.search.search(dic)
        elif choice==6:
            print("exit")
        else:
            print("invalid choice:")        
                   


menu()
        
    
    

