students_data=[]
def signup():
    print("======================================================")
    print("****************STUDENTS DESHBOARD********************")
    print("======================================================")
        
    uid = input("enter the id:")
    name = input("enter the name:")
    rank = input("enter the rank:")
    qualification = input("enter the qualification:")
    email = input("enter the email:")
    password = input("enter the passwor:")
    
    data = {
        "uid":uid,
        "name":name,
        "rank":rank,
        "qualifictaion":qualification,
        "email":email,
        "password":password
        
    }

    students_data.append(data) 
    print("singup is succesfull")  
    
def login():
    email = input("please enter the email:")
    password = input("please enter the password:")
    
    for i in students_data:
        if i["email"]==email and i["password"]==password:
            print(" login succesfull")
            break
        else:
            print("data is not found")
            break            
    
    
    
def menu():
    
    print("==================================================")
    print("*********************menu*************************")
    print("==================================================")
    
    
    while True:    
        print("1. signup")
        print("2. login") 
        print("3. exit")  
        
        choice =input("enter the choice:")
        if choice=="1":
            signup()
        elif choice=="2":
            login()
        elif choice=="3":
            print("exit")
            break
        else:
            print("invalid your choice")
menu()