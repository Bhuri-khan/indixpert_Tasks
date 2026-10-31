

def login(dictionary):


    while True:
    
        email=input(" please Enter Email ID: ")
        if len(email)>6:
            if "@" in email and ".com" in email:
                break
            else:
                print("Invalid Your Email ID")
        else:
            print("Invalid Your Email ID")
    while True:
        password=input("Enter Password: ")
        if len(password)>6:
                if password.isalnum():
                    break
                else:
                    print("Invalid Your Password")
        else:
                print("Please Password 6 Character Greater")
    while True:
        if email==email and password==password:
            print("login succesful")
            dictionary["email"]=email
            dictionary["password"]=password
            print(dictionary)
            
            break
        
        else:
            print("invalid login")
    
            
    