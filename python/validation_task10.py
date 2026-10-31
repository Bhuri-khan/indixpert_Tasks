students = {}


print ("============================================================")
print("********************students dashboard***********************")
print("=============================================================")

def singup():
    uid = int(input("please enter the user id:"))
    name = input("please enter the name:")
    email = input("please enter the email:")
    password = input("please enter the password:")
    con_password = input("please enter the confirm passowrd:")
    
    students.update()
    
    if (uid<0):
        print("invalid uid")
        return
    
    # name = input("please enter the name:")

    if not name.isalpha():
        print("Name is not valid")
        return
    
    if '@' not in email or '.' not in email:
        print("email formate is not valid")
        return
    if len(password)<6 or len(password)>10:
        print(" password  not  valid")
        return

    if (password!=con_password):
        print("conform pasword is not valid")
        return
        
        
    students["uid"]=uid 
    students["name"]=name
    students["email"]=email 
    students["password"]=password
    students["confirm"]=con_password
    print("Sign-up Successful")
            
    
def login():
    print("*****************login*****************")
    
    email = input("enter the email: ")
    password = input("enter the password: ")
    if students["email"]==email and students["password"]==password:
        print("login is succesfully")
        print(students)
        
            
    else:
        print("data is not found")
            
def menu():            
    while True:     
        print("==================menu====================") 
              
        print("1. Signup")
        print("2. Login")
        print("3. Exit")
        
        choice=input("enter your choice: ")
        if choice=="1":
            singup()
        elif choice=="2":
            login()
        elif choice=="3":
            print("exit")
            break
        else:
            print("invalid your choice")
menu()